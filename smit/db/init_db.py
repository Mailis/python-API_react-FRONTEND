import os,sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0,parent_dir)

from db import create_db
from db import create_table

def create_db_and_tables():
    isSucc = create_db.create_db()
    if(isSucc):
        create_table.create_table()
