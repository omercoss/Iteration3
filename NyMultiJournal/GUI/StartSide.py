from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QDateTime
from GUI.PatientProfil import PatientProfil
from GUI.LoginFejl import ForkertLogin as LoginFejl

class StartSide(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 631)
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(70, 40, 671, 531))
        self.listWidget.setObjectName("listWidget")

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(240, 230, 91, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(260, 280, 60, 16))
        self.label_2.setObjectName("label_2")

        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(130, 450, 194, 24))
        self.dateTimeEdit.setObjectName("dateTimeEdit")

        # Opdater dato
        currentDateTime = QDateTime.currentDateTime()
        self.dateTimeEdit.setDateTime(currentDateTime)
        self.dateTimeEdit.setDisplayFormat("dd.MM.yyyy HH:mm")
        self.dateTimeEdit.setMinimumDateTime(currentDateTime)

        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 320, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(170, 100, 421, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 60, 16))
        self.label_3.setObjectName("label_3")

        self.textEdit = QtWidgets.QTextEdit(parent=Form)
        self.textEdit.setGeometry(QtCore.QRect(320, 220, 271, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(parent=Form)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 270, 271, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Tryk på log ind
        self.pushButton.clicked.connect(self.login)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Læge-ID:"))
        self.label_2.setText(_translate("Form", "Kodeord:"))
        self.pushButton.setText(_translate("Form", "Log ind"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600;\">Multi-Electronic-Journal</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "Læge"))

    def login(self):
        # Indsæt værdier for brugernavn og kode i tekstfelter
        username = self.textEdit.toPlainText()
        password = self.textEdit_2.toPlainText()

        # Undersøg om brugernavn og koden er korrekt
        if username == "læge" and password == "123":
            # Hvis login er korrekt går den videre til PatientProfil widget
            self.patient_profil = QtWidgets.QWidget()
            self.patient_profil_ui = PatientProfil()
            self.patient_profil_ui.setupUi(self.patient_profil)
            self.patient_profil.show()

        else:
            # Hvis login er forkert går den videre til LoginFejl widget
            self.loginError = QtWidgets.QWidget()
            self.loginErrorUi = LoginFejl()
            self.loginErrorUi.setupUi(self.loginError)
            self.loginError.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())