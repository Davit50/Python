import sqlite3


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(empId, name, photo, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('image.db')
        cursor = sqliteConnection.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS new_employee(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR,photo BLOB,'
            'resume VARCHAR)')

        empPhoto = convertToBinaryData(photo)
        resume = convertToBinaryData(resumeFile)
        cursor.execute(""" INSERT INTO new_employee
                                  (id, name, photo, resume) VALUES (?, ?, ?, ?)""", (empId, name, empPhoto, resume))
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")


insertBLOB(1, "Davit", "../../istockphoto-1147544807-612x612.jpg", "../../todo.txt")
