# context manager
# with  - pozwala uruchomic context manager
# __enter__, __exit__
import sqlite3


class DBCM:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.commit()
            self.conn.close()


db_name = "my_database.db"

with DBCM(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);")
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Anna",))
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Tom",))

    select = cursor.execute("SELECT * FROM users;")
    for i in select:
        print(i)

# (1, 'John')
# (2, 'John')
# (3, 'Anna')
# (4, 'Tom')
# (5, 'John')
# (6, 'Anna')
# (7, 'Tom')
# (8, 'John')
# (9, 'Anna')
# (10, 'Tom')
# (11, 'John')
# (12, 'Anna')
# (13, 'Tom')
