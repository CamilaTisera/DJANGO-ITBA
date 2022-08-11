from django.db import models
from sqlite3 import dbapi2 as sqlite3

# Create your models here.
def get_data():
    con = sqlite3.connect('db.sqlite3')
    cur = con.cursor()
    cur.execute('SELECT * FROM prueba_prueba')
    return cur.fetchall()

