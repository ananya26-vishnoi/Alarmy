# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'alarm.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(602, 691)
        MainWindow.setStyleSheet("margin:0;\n"
"padding:0;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("margin:0;\n"
"padding:0;\n"
"border:none;")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setStyleSheet("width:100%;\n"
"height:100%;\n"
"margin:0;\n"
"padding:0;\n"
"background-color:#28375f;")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.MainFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.MainFrame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.Header = QtWidgets.QFrame(self.MainFrame)
        self.Header.setMinimumSize(QtCore.QSize(0, 0))
        self.Header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Header.setStyleSheet("background-color:#273250;\n"
"width: 100%;\n"
"margin:0;\n"
"padding:0;")
        self.Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Header.setObjectName("Header")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Header)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.NameFrame = QtWidgets.QFrame(self.Header)
        self.NameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NameFrame.setObjectName("NameFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.NameFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.NameFrame)
        self.label.setMinimumSize(QtCore.QSize(80, 20))
        self.label.setStyleSheet("color:#7f9ee4;\n"
"font-size:22px;")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.NameFrame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.Header)
        self.Title = QtWidgets.QFrame(self.MainFrame)
        self.Title.setStyleSheet("background-color:#28375f;")
        self.Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setLineWidth(0)
        self.Title.setObjectName("Title")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.Title)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.InnerTitle = QtWidgets.QFrame(self.Title)
        self.InnerTitle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InnerTitle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InnerTitle.setObjectName("InnerTitle")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.InnerTitle)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.InnerTitle)
        self.label_3.setStyleSheet("color:#a2b3df;\n"
"font-size:32px;")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.verticalLayout_7.addWidget(self.InnerTitle, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.Title)
        self.AlarmSetting = QtWidgets.QFrame(self.MainFrame)
        self.AlarmSetting.setStyleSheet("background-color:#212a43;")
        self.AlarmSetting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AlarmSetting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AlarmSetting.setObjectName("AlarmSetting")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.AlarmSetting)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.time = QtWidgets.QFrame(self.AlarmSetting)
        self.time.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.time.setFrameShadow(QtWidgets.QFrame.Raised)
        self.time.setObjectName("time")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.time)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.time)
        self.lineEdit.setMaximumSize(QtCore.QSize(40, 40))
        self.lineEdit.setStyleSheet("background-color:white;\n"
"font-size:22px;" "color:black;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.time)
        self.label_4.setStyleSheet("color:white;\n"
"font-size:20px;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.time)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(40, 40))
        self.lineEdit_2.setStyleSheet("background-color:white;\n" "color:black;\n"
"font-size:22px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.verticalLayout_9.addWidget(self.time, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.day = QtWidgets.QFrame(self.AlarmSetting)
        self.day.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.day.setFrameShadow(QtWidgets.QFrame.Raised)
        self.day.setObjectName("day")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.day)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_5 = QtWidgets.QCheckBox(self.day)
        self.checkBox_5.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox_5.setStyleSheet("background-color:#273250;\n"
"color:white;\n"
"border-radius:10px;\n"
"padding:5px;")
        self.checkBox_5.setObjectName("checkBox_5")
        self.horizontalLayout_2.addWidget(self.checkBox_5)
        self.checkBox = QtWidgets.QCheckBox(self.day)
        self.checkBox.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox.setStyleSheet("background-color:#273250;\n"
"color:white;\n"
"border-radius:10px;\n"
"padding:5px;")
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.checkBox_6 = QtWidgets.QCheckBox(self.day)
        self.checkBox_6.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox_6.setStyleSheet("background-color:#273250;\n"
"color:white;\n"
"border-radius:10px;\n"
"padding:5px;")
        self.checkBox_6.setObjectName("checkBox_6")
        self.horizontalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_7 = QtWidgets.QCheckBox(self.day)
        self.checkBox_7.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox_7.setStyleSheet("background-color:#273250;\n"
"color:white;\n"
"border-radius:10px;\n"
"padding:5px;")
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_2.addWidget(self.checkBox_7)
        self.checkBox_2 = QtWidgets.QCheckBox(self.day)
        self.checkBox_2.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox_2.setStyleSheet("padding:5px;\n"
"background-color:#273250;\n"
"color:white;\n"
"border-radius:10px;")
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_2.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.day)
        self.checkBox_3.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox_3.setStyleSheet("background-color:#273250;\n"
"color:white;padding:5px;\n"
"\n"
"border-radius:10px;")
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_2.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.day)
        self.checkBox_4.setMaximumSize(QtCore.QSize(45, 45))
        self.checkBox_4.setStyleSheet("background-color:#273250;\n"
"color:white;\n"
"border-radius:10px;\n"
"padding:5px;")
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout_2.addWidget(self.checkBox_4)
        self.verticalLayout_9.addWidget(self.day, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.AlarmSetting)
        self.SaveButton = QtWidgets.QFrame(self.MainFrame)
        self.SaveButton.setStyleSheet("margin:0")
        self.SaveButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SaveButton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SaveButton.setLineWidth(0)
        self.SaveButton.setObjectName("SaveButton")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.SaveButton)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.SaveButton)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton.setStyleSheet("background-color:#212a43;\n"
"color:#6781b9;\n"
"padding:15px 25px;\n"
"font-size:18px;\n"
"font-weight:600;\n"
"border-radius:5px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.horizontalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.SaveButton)
        self.Info = QtWidgets.QFrame(self.MainFrame)
        self.Info.setStyleSheet("")
        self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Info)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.Info)
        self.label_5.setStyleSheet("color:#a2b3df;\n"
"font-size:32px;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.Info, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Alarmy"))
        self.label_3.setText(_translate("MainWindow", "Set an Alarm"))
        self.label_4.setText(_translate("MainWindow", ":"))
        self.checkBox_5.setText(_translate("MainWindow", "S"))
        self.checkBox.setText(_translate("MainWindow", "M"))
        self.checkBox_6.setText(_translate("MainWindow", "T"))
        self.checkBox_7.setText(_translate("MainWindow", "W"))
        self.checkBox_2.setText(_translate("MainWindow", "T"))
        self.checkBox_3.setText(_translate("MainWindow", "F"))
        self.checkBox_4.setText(_translate("MainWindow", "S"))
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.label_5.setText(_translate("MainWindow", "No Alarms Set"))
