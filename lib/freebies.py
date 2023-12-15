import sqlite3

CONN = sqlite3.connect("./lib/freebies.db")
CURSOR = CONN.cursor()

#! Create Freebies Class
class Freebie():
    def __init__(self, item_name, value, comp_id=None, dev_id=None, id=None):
        self.id = id
        self.item_name = item_name
        self.value = value
        self.comp_id = comp_id
        self.dev_id = dev_id

@classmethod
def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS freebies (
                id INTEGER PRIMARY KEY,
                item_name TEXT,
                value INTEGER,
                comp_id INTEGER,
                dev_id INTEGER
            )
        """
        
        CURSOR.execute(sql)
    
    #! Create a drop table to refresh every time code is ran
@classmethod
def drop_table(cls):
        sql = "DROP TABLE IF EXISTS freebies"
        CURSOR.execute(sql)
    
    #! Create option to save information to Table once created:
def save(self):
    sql = """
        INSERT INTO freebies (item_name, value, comp_id, dev_id)
        VALUES (?, ?, ?, ?)
        """
    CURSOR.execute(sql, (self.item_name, self.value, self.comp_id, self.dev_id))
    CONN.commit()
    self.id = CURSOR.lastrowid    