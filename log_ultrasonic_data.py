import sqlite3
import random
from datetime import datetime
from time import sleep

def create_table():
    query = """CREATE TABLE IF NOT EXISTS ultrasonic(datetime TEXT NOT NULL, distance REAL NOT NULL)"""
    try:
        conn = sqlite3.connect("skraldespand.db")
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"sqlite error: {e}")
    except Exception as e:
        print(f"error: {e}")
    finally:
        conn.close()

def log_ultrasonic_data():
    while True:
        query = """INSERT INTO ultrasonic(datetime, distance) VALUES (?,?)"""
        now = datetime.now()
        now = now.strftime("%d/%m/%y %H:%M:%S")
        data = (now, random.randint(0,40))

        try:
            conn = sqlite3.connect("skraldespand.db")
            cur = conn.cursor()
            cur.execute(query,data)
            conn.commit()
        except sqlite3.Error as e:
            print(f"sqlite3 error: {e}")
            conn.rollback() 
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
        sleep(1)

create_table()
log_ultrasonic_data()