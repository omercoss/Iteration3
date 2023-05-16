'''import mysql.connector'''
from PyQt6 import QtCore, QtWidgets
from GUI.MedicinAdministration import MedicinAdministration
from classes.database import soegCPRnummer as soegImporteret


class PatientProfil(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(740, 526)
        self.textEdit = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit.setGeometry(QtCore.QRect(250, 30, 191, 31))
        self.textEdit.setObjectName("textEdit")

        self.textBrowser = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 80, 311, 101))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(360, 80, 321, 431))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.commandLinkButton = QtWidgets.QCommandLinkButton(parent=Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(530, 470, 141, 31))
        self.commandLinkButton.setObjectName("commandLinkButton")

        self.textEdit_2 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(130, 100, 181, 21))
        self.textEdit_2.setObjectName("textEdit_2")

        self.textEdit_3 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(430, 120, 121, 21))
        self.textEdit_3.setObjectName("textEdit_3")

        self.textEdit_4 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(440, 150, 121, 21))
        self.textEdit_4.setObjectName("textEdit_4")

        self.textEdit_5 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(450, 180, 121, 21))
        self.textEdit_5.setObjectName("textEdit_5")

        self.textEdit_6 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(410, 220, 121, 21))
        self.textEdit_6.setObjectName("textEdit_6")

        self.textEdit_7 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(430, 250, 121, 21))
        self.textEdit_7.setObjectName("textEdit_7")

        self.textEdit_8 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(490, 290, 121, 21))
        self.textEdit_8.setObjectName("textEdit_8")

        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 140, 131, 32))
        self.pushButton.setObjectName("pushButton")

        self.textEdit_9 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_9.setGeometry(QtCore.QRect(460, 320, 121, 21))
        self.textEdit_9.setObjectName("textEdit_9")

        self.textEdit_10 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_10.setGeometry(QtCore.QRect(430, 360, 121, 21))
        self.textEdit_10.setObjectName("textEdit_10")

        self.textEdit_11 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_11.setGeometry(QtCore.QRect(410, 390, 121, 21))
        self.textEdit_11.setObjectName("textEdit_11")

        self.textEdit_12 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_12.setGeometry(QtCore.QRect(420, 420, 121, 21))
        self.textEdit_12.setObjectName("textEdit_12")

        self.textEdit_13 = QtWidgets.QTextEdit(parent=Dialog)
        self.textEdit_13.setGeometry(QtCore.QRect(410, 450, 121, 21))
        self.textEdit_13.setObjectName("textEdit_13")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.vis_oplysninger)
        self.pushButton.clicked.connect(self.soegPatient)

        self.commandLinkButton.clicked.connect(self.MedicinAdministration)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:24pt; font-weight:600; color:#55aaff;\">Patient profil: </span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">CPR-nummer: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\">Almene oplysninger </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-style:italic;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Fornavn:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Efternavn:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Fødselsdag:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Alder:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Adresse:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Telefonnummer: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Sygdomme: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt;\">Allergi:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Køn: </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Højde:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Vægt:</span></p></body></html>"))
        self.commandLinkButton.setText(_translate("Dialog", "Medicinoplysninger"))
        self.pushButton.setText(_translate("Dialog", "Vis oplysninger"))

    def vis_oplysninger(self):
        CPR = self.textEdit_2.toPlainText()

        data = {
            '2610016748': {
                'Fornavn': 'Ömer',
                'Efternavn': 'Coskun',
                'Fødselsdag': '26-10-2001',
                'Alder': '21 år',
                'Adresse': 'Universitetsparken 2',
                'Telefonnummer': '68306738',
                'Sygdomme': 'PTSD / KOL',
                'Allergi': 'Pollen',
                'Køn': 'Mand',
                'Højde': '200 cm',
                'Vægt': '100 kg'
            },
            '1407669376': {
                'Fornavn': 'Sabrina',
                'Efternavn': 'Bibi',
                'Fødselsdag': '14-07-1966',
                'Alder': ' 56 år',
                'Adresse': 'Jagtvej 3',
                'Telefonnummer': '99338822',
                'Sygdomme': 'OCD / Astma',
                'Allergi': 'Husstøvmidler',
                'Køn': 'Kvinder',
                'Højde': '130 cm',
                'Vægt': '50 kg'
            }
        }

        patient_info = data.get(CPR)

        if patient_info:
            self.textEdit_3.setText(patient_info['Fornavn'])
            self.textEdit_4.setText(patient_info['Efternavn'])
            self.textEdit_5.setText(patient_info['Fødselsdag'])
            self.textEdit_6.setText(patient_info['Alder'])
            self.textEdit_7.setText(patient_info['Adresse'])
            self.textEdit_8.setText(patient_info['Telefonnummer'])
            self.textEdit_9.setText(patient_info['Sygdomme'])
            self.textEdit_10.setText(patient_info['Allergi'])
            self.textEdit_11.setText(patient_info['Køn'])
            self.textEdit_12.setText(patient_info['Højde'])
            self.textEdit_13.setText(patient_info['Vægt'])
        else:
            self.textEdit_2.setText('Patient ikke fundet!')

    def soegPatient(self):
        CPRnummer = self.textEdit_2.toPlainText()
        soegImporteret(CPRnummer)

    '''def soegPatient(self):
        input = self.textEdit_2.toPlainText()

        db = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='Amagerkbh1313',
                database='dlm'
        )

        if db.is_connected():
            print("Forbindelse oprettet")
        else:
            print("Ingen forbindelse")

        cursor = db.cursor()

        query = f"SELECT * FROM patientoplysning WHERE CPRnummer = '{input}'"

        cursor.execute(query)

        result = cursor.fetchall()

        if result:
            # Populate the text fields with the retrieved data
            self.textEdit_3.setPlainText(result[1])  # First name
            self.textEdit_4.setPlainText(result[2])  # Last name
            self.textEdit_5.setPlainText(result[3])  # Birthday
            self.textEdit_6.setPlainText(result[4])
            self.textEdit_7.setPlainText(result[5])
            self.textEdit_8.setPlainText(result[6])
            self.textEdit_9.setPlainText(result[7])
            self.textEdit_10.setPlainText(result[8])
            self.textEdit_11.setPlainText(result[9])
            self.textEdit_12.setPlainText(result[10])
            self.textEdit_13.setPlainText(result[11])
        else:
            self.textEdit_2.setText('Patient ikke fundet!')'''

    def MedicinAdministration(self):
        self.widget = QtWidgets.QWidget()
        self.ui = MedicinAdministration()
        self.ui.setupUi(self.widget)
        self.widget.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = PatientProfil()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
