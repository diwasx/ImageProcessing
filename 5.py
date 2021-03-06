# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import math
import numpy as np

fileName=None
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 548)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(380, 40, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btnUp = QtWidgets.QPushButton(Dialog)
        self.btnUp.setGeometry(QtCore.QRect(30, 71, 151, 81))
        self.btnUp.setObjectName("btnUp")
        self.btnNeg = QtWidgets.QPushButton(Dialog)
        self.btnNeg.setGeometry(QtCore.QRect(30, 500, 75, 23))
        self.btnNeg.setObjectName("btnNeg")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(30, 390, 141, 51))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.imgView = QtWidgets.QLabel(Dialog)
        self.imgView.setGeometry(QtCore.QRect(230, 90, 381, 361))
        self.imgView.setText("")
        self.imgView.setObjectName("imgView")
        self.btnLog = QtWidgets.QPushButton(Dialog)
        self.btnLog.setGeometry(QtCore.QRect(120, 500, 75, 23))
        self.btnLog.setObjectName("btnLog")
        self.btnLI = QtWidgets.QPushButton(Dialog)
        self.btnLI.setGeometry(QtCore.QRect(210, 500, 75, 23))
        self.btnLI.setObjectName("btnLI")
        self.btnPow = QtWidgets.QPushButton(Dialog)
        self.btnPow.setGeometry(QtCore.QRect(300, 500, 75, 23))
        self.btnPow.setObjectName("btnPow")
        self.btnRoot = QtWidgets.QPushButton(Dialog)
        self.btnRoot.setGeometry(QtCore.QRect(400, 500, 75, 23))
        self.btnRoot.setObjectName("btnRoot")
        self.btnGray = QtWidgets.QPushButton(Dialog)
        self.btnGray.setGeometry(QtCore.QRect(40, 340, 101, 41))
        self.btnGray.setObjectName("btnGray")
        self.btnOrg = QtWidgets.QPushButton(Dialog)
        self.btnOrg.setGeometry(QtCore.QRect(40, 270, 101, 41))
        self.btnOrg.setObjectName("btnOrg")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        ##
        self.btnNeg.clicked.connect(self.setNeg)
        self.btnUp.clicked.connect(self.setImage)
        self.btnOrg.clicked.connect(self.setOrg)
        self.btnGray.clicked.connect(self.setGray)
        self.btnLog.clicked.connect(self.setLog)
        self.btnPow.clicked.connect(self.setPower)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Image Processing"))
        self.label.setText(_translate("Dialog", "Image"))
        self.btnUp.setText(_translate("Dialog", "Upload"))
        self.btnNeg.setText(_translate("Dialog", "Negative"))
        self.btnLog.setText(_translate("Dialog", "Log"))
        self.btnLI.setText(_translate("Dialog", "LogInverse"))
        self.btnPow.setText(_translate("Dialog", "n power"))
        self.btnRoot.setText(_translate("Dialog", "n root"))
        self.btnGray.setText(_translate("Dialog", "Gray Scale"))
        self.btnOrg.setText(_translate("Dialog", "Original"))

    ##
    def setNeg(self):
        if fileName:
            a=cv2.imread(fileName,1)
            # a = cv2.resize(a, (1024, 768))
            print(fileName)
            print(a)
            neg=255-a
            cv2.imshow('negative',neg)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            

    def setOrg(self):
        if fileName:
            a=cv2.imread(fileName,1)
            print(a) 
            cv2.imshow('original',a)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            
            
    def setGray(self):
        if fileName:
            a=cv2.imread(fileName,0)
            print(a) 
            cv2.imshow('Gray',a)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            

    def setLog(self):
        if fileName:
            a=cv2.imread(fileName,0)
            c=.3
            # s=c*np.log10(1+a)
            s=c*np.uint8(np.log1p(a))
            s=cv2.normalize(s, None, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
            print(s)
            cv2.imshow('Log Transformation',s)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            

    def setLI(self):
        if fileName:
            a=cv2.imread(fileName,1)
            cv2.imshow('original',a)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            

    def setPower(self):
        if fileName:
            a=cv2.imread(fileName,1)
            c=1
            g=0.3
            s=c*pow(a,g)
            print(s)
            s=cv2.normalize(s, None, 0, 255, cv2.NORM_MINMAX, dtype = cv2.CV_8U)
            print(s)
            cv2.imshow('Nth power',s)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            


    def setRoot(self):
        if fileName:
            a=cv2.imread(fileName,1)
            cv2.imshow('original',a)
            cv2.waitKey(0)
        else: 
            print("no file selected")
            

    def setImage(self):
        global fileName
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.imgView.width(), self.imgView.height(), QtCore.Qt.KeepAspectRatio)
            self.imgView.setPixmap(pixmap)
            self.imgView.setAlignment(QtCore.Qt.AlignCenter)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

