# Form implementation generated from reading ui file '.\qt_intro.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt6.QtOpenGLWidgets import QOpenGLWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
import sys



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1241, 806)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.RecordTab = QtWidgets.QWidget()
        self.RecordTab.setObjectName("RecordTab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.RecordTab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.VidFrame = QtWidgets.QFrame(parent=self.RecordTab)
        self.VidFrame.setMinimumSize(QtCore.QSize(1000, 0))
        self.VidFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.VidFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.VidFrame.setObjectName("VidFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.VidFrame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.heading = QtWidgets.QFrame(parent=self.VidFrame)
        self.heading.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.heading.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.heading.setObjectName("heading")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.heading)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(parent=self.heading)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(parent=self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.verticalLayout_3.addWidget(self.heading)
        self.frame = QtWidgets.QFrame(parent=self.VidFrame)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(440, 330))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(440, 330))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout_3.addWidget(self.frame)
        self.CamLabFrame = QtWidgets.QFrame(parent=self.VidFrame)
        self.CamLabFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.CamLabFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CamLabFrame.setObjectName("CamLabFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.CamLabFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(parent=self.CamLabFrame)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.CamLabFrame)
        self.horizontalLayout_5.addWidget(self.VidFrame)
        self.ConFrame = QtWidgets.QFrame(parent=self.RecordTab)
        self.ConFrame.setMinimumSize(QtCore.QSize(200, 0))
        self.ConFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ConFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ConFrame.setObjectName("ConFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ConFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.ConTitle = QtWidgets.QLabel(parent=self.ConFrame)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.ConTitle.setFont(font)
        self.ConTitle.setObjectName("ConTitle")
        self.verticalLayout_4.addWidget(self.ConTitle)
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.ConFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_4.addWidget(self.graphicsView)
        self.horizontalLayout_5.addWidget(self.ConFrame)
        self.tabWidget.addTab(self.RecordTab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.VidFrame_2 = QtWidgets.QFrame(parent=self.tab_2)
        self.VidFrame_2.setMinimumSize(QtCore.QSize(1000, 0))
        self.VidFrame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.VidFrame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.VidFrame_2.setObjectName("VidFrame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.VidFrame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.heading_2 = QtWidgets.QFrame(parent=self.VidFrame_2)
        self.heading_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.heading_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.heading_2.setObjectName("heading_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.heading_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(parent=self.heading_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_10.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.buttonsFrame_2 = QtWidgets.QFrame(parent=self.heading_2)
        self.buttonsFrame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.buttonsFrame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.buttonsFrame_2.setObjectName("buttonsFrame_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.buttonsFrame_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_4 = QtWidgets.QFrame(parent=self.buttonsFrame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.toolButton_4 = QtWidgets.QToolButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_4.setFont(font)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_12.addWidget(self.toolButton_4)
        self.toolButton_5 = QtWidgets.QToolButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_5.setFont(font)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_12.addWidget(self.toolButton_5)
        self.toolButton_6 = QtWidgets.QToolButton(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_6.setFont(font)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_12.addWidget(self.toolButton_6)
        self.horizontalLayout_11.addWidget(self.frame_4)
        self.verticalLayout_6.addWidget(self.buttonsFrame_2)
        self.verticalLayout_5.addWidget(self.heading_2)
        self.frame_5 = QtWidgets.QFrame(parent=self.VidFrame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtWidgets.QLabel(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(440, 330))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.label_9 = QtWidgets.QLabel(parent=self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(440, 330))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(parent=self.VidFrame_2)
        self.frame_6.setMinimumSize(QtCore.QSize(440, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.progressBar_3 = QtWidgets.QProgressBar(parent=self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_3.sizePolicy().hasHeightForWidth())
        self.progressBar_3.setSizePolicy(sizePolicy)
        self.progressBar_3.setMinimumSize(QtCore.QSize(440, 0))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.horizontalLayout_14.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(parent=self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar_4.sizePolicy().hasHeightForWidth())
        self.progressBar_4.setSizePolicy(sizePolicy)
        self.progressBar_4.setMinimumSize(QtCore.QSize(440, 0))
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.horizontalLayout_14.addWidget(self.progressBar_4)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.CamLabFrame_2 = QtWidgets.QFrame(parent=self.VidFrame_2)
        self.CamLabFrame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.CamLabFrame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.CamLabFrame_2.setObjectName("CamLabFrame_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.CamLabFrame_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_7 = QtWidgets.QLabel(parent=self.CamLabFrame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(parent=self.CamLabFrame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_15.addWidget(self.label_8)
        self.verticalLayout_5.addWidget(self.CamLabFrame_2)
        self.horizontalLayout_16.addWidget(self.VidFrame_2)
        self.frame_2 = QtWidgets.QFrame(parent=self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.ConFrame_2 = QtWidgets.QFrame(parent=self.frame_2)
        self.ConFrame_2.setGeometry(QtCore.QRect(0, 21, 200, 781))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConFrame_2.sizePolicy().hasHeightForWidth())
        self.ConFrame_2.setSizePolicy(sizePolicy)
        self.ConFrame_2.setMinimumSize(QtCore.QSize(200, 0))
        self.ConFrame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.ConFrame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.ConFrame_2.setObjectName("ConFrame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ConFrame_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ConTitle_2 = QtWidgets.QLabel(parent=self.ConFrame_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.ConTitle_2.setFont(font)
        self.ConTitle_2.setObjectName("ConTitle_2")
        self.verticalLayout_7.addWidget(self.ConTitle_2)
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=self.ConFrame_2)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_7.addWidget(self.graphicsView_2)
        self.horizontalLayout_16.addWidget(self.frame_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.centralFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.centralFrame.setMinimumSize(QtCore.QSize(1100, 0))
        self.centralFrame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.centralFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.centralFrame.setObjectName("centralFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.centralFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout.addWidget(self.centralFrame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1241, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionDraw_Detection = QtWidgets.QAction(parent=MainWindow)
        self.actionDraw_Detection.setObjectName("actionDraw_Detection")
        self.actionDelete_Detection = QtWidgets.QAction(parent=MainWindow)
        self.actionDelete_Detection.setObjectName("actionDelete_Detection")
        self.actionSave_2 = QtWidgets.QAction(parent=MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSave_As_2 = QtWidgets.QAction(parent=MainWindow)
        self.actionSave_As_2.setObjectName("actionSave_As_2")
        self.actionSettings = QtWidgets.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionSettings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "MightyMicros Camera Feed"))
        self.label.setText(_translate("MainWindow", "Microtome Camera Feed"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "Start Recording"))
        self.ConTitle.setText(_translate("MainWindow", "Console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.RecordTab), _translate("MainWindow", "Tab 1"))
        self.label_5.setText(_translate("MainWindow", "MightyMicros Camera Feed"))
        self.label_6.setText(_translate("MainWindow", "Microtome Camera Feed"))
        self.toolButton_4.setText(_translate("MainWindow", "Draw Detection"))
        self.toolButton_5.setText(_translate("MainWindow", "Delete Detection"))
        self.toolButton_6.setText(_translate("MainWindow", "Examine Detection"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_7.setText(_translate("MainWindow", "Camera 1 Timeline"))
        self.label_8.setText(_translate("MainWindow", "Camera 2 Timeline"))
        self.ConTitle_2.setText(_translate("MainWindow", "Console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As..."))
        self.actionDraw_Detection.setText(_translate("MainWindow", "Draw Detection"))
        self.actionDelete_Detection.setText(_translate("MainWindow", "Delete Detection"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_As_2.setText(_translate("MainWindow", "Save As..."))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))

# Put this at the end ----------------------------------------
class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MyMainWindow()
    mainWin.show()
    sys.exit(app.exec())
