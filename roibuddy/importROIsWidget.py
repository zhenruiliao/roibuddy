# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importROIsWidget.ui'
#
# Created: Mon Jan  5 21:14:28 2015
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_importROIsWidget(object):
    def setupUi(self, importROIsWidget):
        importROIsWidget.setObjectName(_fromUtf8("importROIsWidget"))
        importROIsWidget.resize(462, 430)
        self.verticalLayout = QtGui.QVBoxLayout(importROIsWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_7 = QtGui.QLabel(importROIsWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_4 = QtGui.QLabel(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.sourceDataset = QtGui.QComboBox(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceDataset.sizePolicy().hasHeightForWidth())
        self.sourceDataset.setSizePolicy(sizePolicy)
        self.sourceDataset.setObjectName(_fromUtf8("sourceDataset"))
        self.gridLayout.addWidget(self.sourceDataset, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.targetChannel = QtGui.QComboBox(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetChannel.sizePolicy().hasHeightForWidth())
        self.targetChannel.setSizePolicy(sizePolicy)
        self.targetChannel.setObjectName(_fromUtf8("targetChannel"))
        self.gridLayout.addWidget(self.targetChannel, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.sourceLabel = QtGui.QComboBox(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceLabel.sizePolicy().hasHeightForWidth())
        self.sourceLabel.setSizePolicy(sizePolicy)
        self.sourceLabel.setObjectName(_fromUtf8("sourceLabel"))
        self.gridLayout.addWidget(self.sourceLabel, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.sourceChannel = QtGui.QComboBox(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourceChannel.sizePolicy().hasHeightForWidth())
        self.sourceChannel.setSizePolicy(sizePolicy)
        self.sourceChannel.setObjectName(_fromUtf8("sourceChannel"))
        self.gridLayout.addWidget(self.sourceChannel, 1, 1, 1, 1)
        self.label = QtGui.QLabel(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(importROIsWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.copyRoiProperties = QtGui.QCheckBox(importROIsWidget)
        self.copyRoiProperties.setText(_fromUtf8(""))
        self.copyRoiProperties.setObjectName(_fromUtf8("copyRoiProperties"))
        self.gridLayout.addWidget(self.copyRoiProperties, 5, 1, 1, 1)
        self.targetLabel = QtGui.QLineEdit(importROIsWidget)
        self.targetLabel.setObjectName(_fromUtf8("targetLabel"))
        self.gridLayout.addWidget(self.targetLabel, 4, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(importROIsWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.label_9 = QtGui.QLabel(importROIsWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_10 = QtGui.QLabel(importROIsWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.registrationMethod = QtGui.QComboBox(importROIsWidget)
        self.registrationMethod.setObjectName(_fromUtf8("registrationMethod"))
        self.gridLayout_3.addWidget(self.registrationMethod, 1, 1, 1, 1)
        self.label_8 = QtGui.QLabel(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_3.addWidget(self.label_8, 0, 0, 1, 1)
        self.auto_manual = QtGui.QComboBox(importROIsWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auto_manual.sizePolicy().hasHeightForWidth())
        self.auto_manual.setSizePolicy(sizePolicy)
        self.auto_manual.setObjectName(_fromUtf8("auto_manual"))
        self.gridLayout_3.addWidget(self.auto_manual, 0, 1, 1, 1)
        self.label_11 = QtGui.QLabel(importROIsWidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 2, 0, 1, 1)
        self.polynomialOrder = QtGui.QLineEdit(importROIsWidget)
        self.polynomialOrder.setObjectName(_fromUtf8("polynomialOrder"))
        self.gridLayout_3.addWidget(self.polynomialOrder, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.acceptButton = QtGui.QPushButton(importROIsWidget)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.horizontalLayout.addWidget(self.acceptButton)
        self.cancelButton = QtGui.QPushButton(importROIsWidget)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout.addWidget(self.cancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(importROIsWidget)
        QtCore.QMetaObject.connectSlotsByName(importROIsWidget)

    def retranslateUi(self, importROIsWidget):
        importROIsWidget.setWindowTitle(_translate("importROIsWidget", "Form", None))
        self.label_7.setText(_translate("importROIsWidget", "Transform and copy ROIs to new Imaging Dataset", None))
        self.label_4.setText(_translate("importROIsWidget", "Source Label:", None))
        self.label_2.setText(_translate("importROIsWidget", "Source Channel:", None))
        self.label_3.setText(_translate("importROIsWidget", "Target Channel:", None))
        self.label_5.setText(_translate("importROIsWidget", "Target Label:", None))
        self.label.setText(_translate("importROIsWidget", "Source Imaging Dataset:", None))
        self.label_6.setText(_translate("importROIsWidget", "Copy ROI properties:", None))
        self.label_9.setText(_translate("importROIsWidget", "Registration Parameters", None))
        self.label_10.setText(_translate("importROIsWidget", "Method", None))
        self.label_8.setText(_translate("importROIsWidget", "Auto or Manual:", None))
        self.label_11.setText(_translate("importROIsWidget", "Order", None))
        self.acceptButton.setText(_translate("importROIsWidget", "Import ROIs", None))
        self.cancelButton.setText(_translate("importROIsWidget", "Cancel", None))

