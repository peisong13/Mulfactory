import sqlite3
from logger import logger

DB_NAME = 'example.db'
TABLE_NAME = 'task_table'

if __name__ == '__main__':
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f'select * from {TABLE_NAME}')
    tasks = cursor.fetchall()
    conn.close()

    print(tasks)