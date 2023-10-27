# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'venv/change_dir_time.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os, random
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:

    def _fromUtf8(s):
        return s


try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_widget(object):

    def setupUi(self, widget):
        widget.setObjectName(_fromUtf8("widget"))
        widget.resize(114, 120)
        self.verticalLayout = QtGui.QVBoxLayout(widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lineEdit = QtGui.QLineEdit(widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.getDirButton = QtGui.QPushButton(widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.getDirButton.sizePolicy().hasHeightForWidth())
        self.getDirButton.setSizePolicy(sizePolicy)
        self.getDirButton.setObjectName(_fromUtf8("getDirButton"))
        self.verticalLayout.addWidget(self.getDirButton)
        self.dateEdit = QtGui.QDateEdit(widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        self.dateEdit.setDateTime(
            QtCore.QDateTime(QtCore.QDate(2023, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.verticalLayout.addWidget(self.dateEdit)
        self.startButton = QtGui.QPushButton(widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.verticalLayout.addWidget(self.startButton)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

        self.chooseDate = 1672502400
        self.getDirButton.clicked.connect(self.handleGetDir)
        self.startButton.clicked.connect(self.handleStartChange)

    def retranslateUi(self, widget):
        widget.setWindowTitle(_translate("widget", "修改文件时间", None))
        self.getDirButton.setText(_translate("widget", "选择文件夹", None))
        self.startButton.setText(_translate("widget", "开始", None))

    def handleGetDir(self):
        dirName = QtGui.QFileDialog.getExistingDirectory(
            None, _translate("Form", "请选择文件夹", None), "")
        self.lineEdit.setText(dirName)

    def handleStartChange(self):
        self.chooseDate = self.dateEdit.dateTime().toTime_t()
        if os.path.exists(unicode(self.lineEdit.text())):
            for root, dirs, files in os.walk(unicode(self.lineEdit.text())):
                for f in files:
                    if os.stat(os.path.join(root,
                                            f)).st_mtime >= self.chooseDate:
                        setRandomDate = self.chooseDate - round(
                            random.uniform(8 * 60 * 60, 16 * 60 * 60), 2)
                        os.utime(os.path.join(root, f),
                                 (setRandomDate, setRandomDate))
                for d in dirs:
                    if os.stat(os.path.join(root,
                                            d)).st_mtime >= self.chooseDate:
                        setRandomDate = self.chooseDate - round(
                            random.uniform(4 * 60 * 60, 8 * 60 * 60), 2)
                        os.utime(os.path.join(root, d),
                                 (setRandomDate, setRandomDate))
            QtGui.QMessageBox.about(None, 'about',
                                    _translate("Form", "完成修改", None))
        else:
            QtGui.QMessageBox.about(None, 'about',
                                    _translate("Form", "请选择文件夹", None))


import sys

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
ui = Ui_widget()
ui.setupUi(widget)
widget.show()
sys.exit(app.exec_())
