import sqlite3
from freebies import Freebie

CONN = sqlite3.connect("./lib/freebies.db")
CURSOR = CONN.cursor()

class Company():
    def __init__(self, name, founding_year, id=None):
        self.set_name(name)
        self.founding_year = founding_year
        self.id = id
        

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str and len(new_name) > 0:
            self._name = new_name
        else: 
            print("name is not a string")
            raise Exception()
    
    name = property(get_name, set_name)
@classmethod
def create_table(cls):
    sql = """
        CREATE TABLE IF NOT EXISTS companies (
         id INTEGER PRIMARY KEY,
            name TEXT,
            founding_year INTEGER  
            )
        """
    CURSOR.execute(sql)
    
@classmethod
def drop_table(cls):
    sql = "DROP TABLE IF EXISTS companies"
    CURSOR.execute(sql)
        
    
def save(self):
    sql = """
        INSERT INTO companies (name, founding_year)
        VALUES (?, ?)
        """
    CURSOR.execute(sql, (self.name, self.founding_year))
    CONN.commit()
    self.id = CURSOR.lastrowid