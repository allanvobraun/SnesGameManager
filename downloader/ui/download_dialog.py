# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/allan/PycharmProjects/pyqt/downloader/ui/download_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DownloadDialog(object):
    def setupUi(self, DownloadDialog):
        DownloadDialog.setObjectName("DownloadDialog")
        DownloadDialog.resize(370, 246)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DownloadDialog.sizePolicy().hasHeightForWidth())
        DownloadDialog.setSizePolicy(sizePolicy)
        self.progressBar = QtWidgets.QProgressBar(DownloadDialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 110, 351, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.buttonBox = QtWidgets.QDialogButtonBox(DownloadDialog)
        self.buttonBox.setGeometry(QtCore.QRect(144, 210, 80, 25))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DownloadDialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.retranslateUi(DownloadDialog)
        self.buttonBox.accepted.connect(DownloadDialog.accept)
        self.buttonBox.rejected.connect(DownloadDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DownloadDialog)

    def retranslateUi(self, DownloadDialog):
        _translate = QtCore.QCoreApplication.translate
        DownloadDialog.setWindowTitle(_translate("DownloadDialog", "Dialog"))
        self.label.setText(_translate("DownloadDialog", "Downloading images"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DownloadDialog = QtWidgets.QDialog()
    ui = Ui_DownloadDialog()
    ui.setupUi(DownloadDialog)
    DownloadDialog.show()
    sys.exit(app.exec_())

