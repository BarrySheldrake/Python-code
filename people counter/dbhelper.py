import sqlite3

class DBHelper:
    def __init__(self, dbname="counter.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        tblstmt = "CREATE TABLE IF NOT EXISTS items (date, time, count)"
        self.conn.execute(tblstmt)
        self.conn.commit()

    def add_record(self, date, time, count):
        stmt = "INSERT INTO items (date, time, count) VALUES (?, ?, ?)"
        args = (date, time, count)
        self.conn.execute(stmt, args)
        self.conn.commit()
