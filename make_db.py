from sqlalchemy import create_engine
import sqlite3




engine = create_engine("sqlite:///users.db")
Session = sessionmaker(engine)



def get_db_connection():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS my_info (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    """)
    conn.commit()
    conn.close()


create_table()
