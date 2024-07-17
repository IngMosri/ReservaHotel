import sqlite3

def create_connection():
    connection = sqlite3.connect("hotel_reservations.db")
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS reservations (
                      id INTEGER PRIMARY KEY,
                      name TEXT NOT NULL,
                      room_type TEXT NOT NULL,
                      check_in_date TEXT NOT NULL,
                      check_out_date TEXT NOT NULL)''')
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_table()
