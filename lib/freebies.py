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
        