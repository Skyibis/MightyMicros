import os
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtMultimedia import *
import cv2
import numpy as np
from sys import settrace, stdout, stderr
import queue

from src import PROJECT_ROOT
from src.pipeline.model import Model
# from src.entry import StreamToLogger


import logging

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('YOLO_Detection')


def my_tracer(frame, event, arg = None): 
    # extracts frame code 
    code = frame.f_code 
  
    # extracts calling function name 
    func_name = code.co_name 
  
    # extracts the line number 
    line_no = frame.f_lineno 
  
    print(f"A {event} encountered in {func_name}() at line number {line_no} ") 
  
    return my_tracer



# def draw_text(image, number, position=(50, 50), font_scale=1, color=(255, 0, 0), thickness=2, font=cv2.FONT_HERSHEY_SIMPLEX):
#     """
#     Draw a number as text on an image using OpenCV.

#     :param image: The image on which to draw the text.
#     :param number: The number to be drawn as text.
#     :param position: The position where the text starts (bottom-left corner).
#     :param font_scale: Font scale factor that is multiplied by the font-specific base size.
#     :param color: Color of the text in BGR format (blue, green, red).
#     :param thickness: Thickness of the lines used to draw the text.
#     :param font: Font type.
#     :return: Image with the number drawn as text.
#     """
#     # Convert the number to a string
#     text = str(number)

#     # Put the text on the image
#     image = cv2.putText(image, text, position, font, font_scale, color, thickness)

#     return image


class VideoThread(QThread):
    frame_signal = pyqtSignal(QImage)
    camera_failed_signal = pyqtSignal(int)
    console_signal = pyqtSignal(str)
    
    def __init__(self, camera_index: int, parent=None):
        super().__init__()
        self.camera = cv2.VideoCapture(camera_index)
        self.camera_index = camera_index
        self.model = Model(os.path.join(PROJECT_ROOT, 'pipeline', 'weights', 'epoch_30.pth'))
        self.save_path = os.path.join(PROJECT_ROOT, 'recordings')
        self.thread_active = True
        self.video_writer = None
        self.is_recording = False
        self.numSlices = 1
        self.detectedSlices = [] # Temporary measure until detection code is fixed
        self.setObjectName(f"VideoThread_{camera_index}")
        logger.info(f'VideoThread initialized with camera index {self.camera_index}')
    
    def run(self):
        logging.info(f'VideoThread running')
        while self.thread_active:
            success, frame = self.camera.read()
            if success:
                frame = cv2.resize(frame, (640, 480))
                annotated_frame = self.model.predict(frame)
                
                #output slice number detected to console
                # if self.camera_index == 0: 
                for detection in self.model.manager.detections.values():                  
                    if detection.id not in self.detectedSlices:
                        self.console_signal.emit(f"Camera {self.camera_index}: Slice {str(detection.id)} detected" )
                        self.detectedSlices.append(detection.id)

                if self.is_recording:
                    try:
                        self.video_writer.write(annotated_frame)
                    except Exception as e:
                        logger.info(f'Error writing frame to video file: {e}')
                        self.stop_recording()
                        
                annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
                qt_frame = QImage(annotated_frame.data, annotated_frame.shape[1], annotated_frame.shape[0], QImage.Format.Format_RGB888)
                qt_frame = qt_frame.scaled(640, 480, Qt.AspectRatioMode.KeepAspectRatio)
                self.frame_signal.emit(qt_frame)
            
            # This was an attempt to fix the camera freezing midway through issue
            if self.camera.isOpened() == False:
                self.camera.release()
                logger.info(f'released camera {self.camera_index}')
                self.camera_failed_signal.emit(self.camera_index)
    
    
    
    def start_recording(self, video_number: int):
        logger.info(f"Camera {self.camera_index} starting recording")
        if not self.is_recording:
            # TODO: Hardcoded 0 for camera number because camera_index is currently a path to a data file for testing. Should be set back to {self.camera_index} when we are using real cameras.
            self.video_writer = cv2.VideoWriter(os.path.join(self.save_path, f'video_recording_{self.camera_index}_{video_number}.mp4'), cv2.VideoWriter_fourcc(*'mp4v'), 10, (640, 480))
            logger.info(f"Video Writer Initialized: {self.video_writer}")
            self.is_recording = True
            
    def stop_recording(self):
        logger.info(f"Camera {self.camera_index} stopping recording")
        if self.is_recording:
            logger.info("Video Writer Released")
            self.is_recording = False
            self.video_writer.release()
            self.video_writer = None
    
    def stop(self):
        self.thread_active = False
        self.camera.release()
        try:
            self.video_writer.release()
        except Exception as e:
            pass
        self.quit()
        self.wait()