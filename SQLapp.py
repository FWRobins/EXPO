import sqlite3

def create_table():
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS expo (id INTEGER PRIMARY KEY NOT NULL, barcode INTEGER NOT NULL UNIQUE, name TEXT NOT NULL, school TEXT, title TEXT NOT NULL, checked BOOL NOT NULL)")
    conn.commit()
    conn.close()
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS barcodes (id INTEGER PRIMARY KEY NOT NULL, barcode INTEGER NOT NULL)")

    # add barcodes from .csv file

    # barcodes = open('barcodes.csv', 'r')
    # contents = barcodes.readlines()
    # for row in contents[1:]:
    #     cur.execute("INSERT INTO barcodes VALUES(NULL,?)", ([row[:-1]]))
    conn.commit()
    conn.close()


def show_data():
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM expo")
    rows=cur.fetchall()
    conn.close()
    return rows

def search_data(barcode="", name="", school="", title="", checked=""):
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM expo WHERE barcode=? OR name=? OR title=?", (barcode, name, title))
    rows=cur.fetchall()
    conn.close()
    return rows

def search_barcodedata(barcode="", name="", school="", title="", checked=""):
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("SELECT barcode FROM barcodes")
    rows=cur.fetchall()
    conn.close()
    return rows

def insert_data(barcode, name, school, title):
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO expo VALUES(NULL,?,?,?,?,?)", (barcode, name, school, title, 'FALSE'))
    conn.commit()
    conn.close()

def update_data(id, barcode, name, school, title):
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("UPDATE expo SET barcode=?, name=?, school=?, title=?, checked=? WHERE id=?", (barcode, name, school, title, 'TRUE', id))
    conn.commit()
    conn.close()

def delete_data(barcode):
    conn=sqlite3.connect("db1.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM barcodes WHERE barcode=?", (barcode,))
    conn.commit()
    conn.close()


create_table()
#insert_data("The Sun", "John Doe", 1918, 913123132)
#delete_data(8)
#update_data(11, 6, "Water Glass")
#print(show_data())
