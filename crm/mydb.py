# To enable touch command use this:-
# Set-Alias -Name touch -Value New-Item

# Install MySQL on my computer
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pass123',
    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE crm_db")

print("All Done")
