import sqlite3
from logger import logger

DB_NAME = 'example.db'
TABLE_NAME = 'task_table'

def init_db(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # create table
    cursor.execute(f'DROP TABLE IF EXISTS {TABLE_NAME};') # uncomment this line to drop the table 
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NAME TEXT, 
                   STATUS INT
                   );''')

    # insert some data
    for i in range(10):
        cursor.execute(f"INSERT INTO {TABLE_NAME} (NAME, STATUS) VALUES ('task{i}', 0);")

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db(DB_NAME)
    logger.info('Database initialized!')