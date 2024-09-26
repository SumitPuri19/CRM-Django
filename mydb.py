import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Scp@2003',
    auth_plugin='mysql_native_password'

    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE dcrm")

print("ALL DONE")

#admin@1234