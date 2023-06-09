from PyQt6 import QtCore, QtWidgets
from GUI.Vejledning import Vejledning
from GUI.Advarsel import Advarsel
from GUI.Oplysning import Oplysning

class MedicinAdministration(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 473)
        self.textBrowser = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(170, 10, 221, 31))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 60, 431, 401))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doubleSpinBox.setGeometry(QtCore.QRect(270, 100, 62, 22))
        self.doubleSpinBox.setObjectName("doubleSpinBox")

        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(270, 200, 62, 22))
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")

        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(parent=Dialog)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(270, 300, 62, 22))
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")

        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 410, 161, 32))
        self.pushButton.setObjectName("pushButton")

        self.toolButton = QtWidgets.QToolButton(parent=Dialog)
        self.toolButton.setGeometry(QtCore.QRect(350, 100, 81, 22))
        self.toolButton.setObjectName("toolButton")

        self.toolButton_2 = QtWidgets.QToolButton(parent=Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(350, 200, 81, 22))
        self.toolButton_2.setObjectName("toolButton_2")

        self.toolButton_3 = QtWidgets.QToolButton(parent=Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(350, 300, 81, 22))
        self.toolButton_3.setObjectName("toolButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Connect the ToolButtons to their respective help dialogs
        self.toolButton.clicked.connect(self.vis_vejledning)
        self.toolButton_2.clicked.connect(self.vis_vejledning)
        self.toolButton_3.clicked.connect(self.vis_vejledning)

        # Connect the Accept Changes button to the method for validating and applying changes
        self.pushButton.clicked.connect(self.accepter)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:600;\">Medicin administration</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdom1 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Medicin1 = </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Ændre dosering</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdom2</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Medicin2 = </span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Ændre dosering</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdom3</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Medicin3 =</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\"> Ændre dosering</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Accepter ændringer"))
        self.toolButton.setText(_translate("Dialog", "Vejledning"))
        self.toolButton_2.setText(_translate("Dialog", "Vejledning"))
        self.toolButton_3.setText(_translate("Dialog", "Vejledning"))

    def vis_vejledning(self):
        self.vejledning_widget = QtWidgets.QWidget()
        self.vejledning_widget_ui = Vejledning()
        self.vejledning_widget_ui.setupUi(self.vejledning_widget)
        self.vejledning_widget.show()

    def accepter(self):
        # Get the values of the three doubleSpinBoxes for the medication dosages
        med1_dosering = self.doubleSpinBox.value()
        med2_dosering = self.doubleSpinBox_2.value()
        med3_dosering = self.doubleSpinBox_3.value()

        # Check if the dosage values are within the range of 1 to 5
        if med1_dosering < 1 or med1_dosering > 5 or \
           med2_dosering < 1 or med2_dosering > 5 or \
           med3_dosering < 1 or med3_dosering > 5:

            # Show an alert message box and return to the medication dosage widget
            self.advarsel_widget = QtWidgets.QWidget()
            self.advarsel_widget_ui = Advarsel()
            self.advarsel_widget_ui.setupUi(self.advarsel_widget)
            self.advarsel_widget.show()

        else:
            # Show a confirmation message box and return to the medication dosage widget if the user confirms
            self.oplysning_widget = QtWidgets.QWidget()
            self.oplysning_widget_ui = Oplysning()
            self.oplysning_widget_ui.setupUi(self.oplysning_widget)
            self.oplysning_widget.show()









if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
