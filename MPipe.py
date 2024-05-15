from multiprocessing import Process, Queue, Lock
import sqlite3
from logger import logger

DB_NAME = 'example.db'
TABLE_NAME = 'task_table'

def main():
    num_processes = 4
    
    queue = Queue()
    lock = Lock()
    
    # get tasks from the database
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(f'select * from {TABLE_NAME} where STATUS <= 0;')
    tasks = cursor.fetchall()
    conn.close()

    # add tasks to the queue
    for task in tasks:
        queue.put(task)

    # create processes
    process_list = [Process(target=worker, args=(queue, lock)) for _ in range(num_processes)]

    # start processes
    for process in process_list:
        process.start()
    
    # wait for processes to finish
    for process in process_list:
        process.join()

def worker(queue, lock):
    conn = sqlite3.connect(DB_NAME)
    conn.execute('PRAGMA journal_mode=WAL;') # use WAL mode to allow multiple readers

    cursor = conn.cursor()
    
    while not queue.empty():
        try:
            task = queue.get()

            # ########### TASK HERE ############

            id, name, status = task

            print(id, name)

            with lock: # use lock to operate on the database
                conn.execute(f'update {TABLE_NAME} set STATUS = 1 where ID = {id};')
                conn.commit() # don't forget to commit

            logger.info(f'Finished a task!')

            # ##################################
        except Exception as e:
            logger.error(f'Error: {repr(e)}')
            with lock:
                conn.execute(f'update {TABLE_NAME} set STATUS = -1 where ID = {id};')
                conn.commit()

    conn.close()

if __name__ == '__main__':
    # init_db(DB_NAME)
    main()