import sqlite3
import threading
import datetime

# Thread-local storage for database connections and cursors
thread_local = threading.local()

# Function to get a database connection for the current thread
def get_db_connection():
    if not hasattr(thread_local, "connection"):
        thread_local.connection = sqlite3.connect('data.db')
    return thread_local.connection

# Function to get a cursor for the current thread
def get_db_cursor():
    if not hasattr(thread_local, "cursor"):
        thread_local.cursor = get_db_connection().cursor()
    return thread_local.cursor

# Fxn
def create_page_visited_table():
    cursor = get_db_cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT,timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename, timeOfvisit):
    cursor = get_db_cursor()
    cursor.execute('INSERT INTO pageTrackTable(pagename,timeOfvisit) VALUES(?,?)', (pagename, timeOfvisit))
    get_db_connection().commit()

def view_all_page_visited_details():
    cursor = get_db_cursor()
    cursor.execute('SELECT * FROM pageTrackTable')
    data = cursor.fetchall()
    return data

# Fxn To Track Input & Prediction
def create_emotionclf_table():
    cursor = get_db_cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT,prediction TEXT,probability NUMBER,timeOfvisit TIMESTAMP)')

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    cursor = get_db_cursor()
    cursor.execute('INSERT INTO emotionclfTable(rawtext,prediction,probability,timeOfvisit) VALUES(?,?,?,?)', (rawtext, prediction, probability, timeOfvisit))
    get_db_connection().commit()

def view_all_prediction_details():
    cursor = get_db_cursor()
    cursor.execute('SELECT * FROM emotionclfTable')
    data = cursor.fetchall()
    return data