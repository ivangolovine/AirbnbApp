import mysql.connector
from mysql.connector import errorcode
import os
from dotenv import load_dotenv

def connect_db():
    load_dotenv(dotenv_path="secrets/.env")
    userNameDB = os.getenv('USERNAMEDB')
    passwordDB = os.getenv('PASSWORDDB')
    hostDB = os.getenv('HOST')
    databaseName = os.getenv('DBNAME')
    
    try:
        cnx = mysql.connector.connect(user=userNameDB,
                                    password=passwordDB,
                                    host=hostDB,
                                    database=databaseName)
        print("Successfully connected to the db")
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None


def add_basic_message(cnx, msgDict):
    if cnx is None:
        print("Database connection is not established.")
        return
    
    cursor = cnx.cursor()
    user_id = msgDict.get('user_id')
    msg = msgDict.get('msg')
    keywords = msgDict.get('keywords')
    delay = msgDict.get('delay')
    
    msg_query = "INSERT INTO messages (user_id, message, Delay, keywords) VALUES (%s, %s, %s, %s)"
    msg_data = (user_id, msg, delay, keywords)
    
    print("Adding message")
    print(msg_query)
    print(msg_data)
    
    try:
        cursor.execute(msg_query, msg_data)
        cnx.commit()
        print("Message added successfully")
    except mysql.connector.Error as err:
        print("Error adding message:", err)
    
    cursor.close()

def add_messages_db(cnx, user_id, message):
    if cnx is None:
        print("Database connection is not established.")
        return
    
    cursor = cnx.cursor()
    add_message_query = ("INSERT INTO messages (user_id, message) VALUES (%s, %s)")
    message_data = (user_id, message)
    
    try:
        cursor.execute(add_message_query, message_data)
        cnx.commit()
        print("Message added successfully.")
    except mysql.connector.Error as err:
        print("Error adding message:", err)
    
    cursor.close()
    
