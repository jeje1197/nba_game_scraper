import mysql.connector

def createDb():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE nbadb")
    mycursor.close()

def createTable():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="nbadb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE mypredictions (date VARCHAR(20), team1 VARCHAR(40), team2 VARCHAR(20), prediction VARCHAR(20))")
    mycursor.close()

def insertData(data:list[dict]):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="nbadb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM mypredictions")
    mydb.commit()

    for entry in data:
        sql = "INSERT INTO mypredictions (date, team1, team2, prediction) VALUES (%s, %s, %s, %s)"
        val = (entry['Date'], entry['Teams'][0], entry['Teams'][1], entry['Prediction'])
        mycursor.execute(sql, val)
        mydb.commit()

    mycursor.close()

def readData():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="nbadb"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM mypredictions")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
