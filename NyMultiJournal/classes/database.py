import mysql.connector

db = mysql.connector.connect(
    user='root',
    password='Amagerkbh1313',
    host='127.0.0.1',
    database='dlm'
)

def soegCPRnummer(input):
    if db.is_connected():
        print("Forbindelse oprettet")
    else:
        print("Ingen forbindelse")

    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM patientoplysning WHERE CPRnummer = '{input}'")
    results = cursor.fetchall()

    if results:
        patient_info = {
            "CPRnummer": results[0],
            "Fornavn": results[1],
            "Efternavn": results[2],
            "Fødselsdag": results[3],
            "Alder": results[4],
            "Adresse": results[5],
            "Telefonnummer": results[6],
            "Sygdomme": results[7],
            "Allergi": results[8],
            "Køn": results[9],
            "Højde": results[10],
            "Vægt": results[11]
        }
        return patient_info
    else:
        print("Ingen patient fundet")

