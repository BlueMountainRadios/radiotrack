"""
Programmer: BlueMountainRadios
Date: 10/09/2026
Version: 1
"""

import sqlite3

class Database:

    def __init__(self):
        # Connect to database.
        self.conn = sqlite3.connect("")

    def get_item(self):
        pass

    def add_item(self):
        pass

    def update_item(self):
        pass

    def close_connection(self):
        self.conn.close()
