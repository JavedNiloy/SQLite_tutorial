import sqlite3 as sql


# initiate database
def init_dbase():
    # connect the database
    conn = sql.connect("customer.db")
    # create cursor
    cursor = conn.cursor()
    return conn, cursor

# create a table
def create_table():
    conn, cursor = init_dbase()
    cursor.execute("""CREATE TABLE customers (
                  first_name text,
                  last_name text,
                  email text
                )""")
    conn.commit()
    conn.close()

# Many entry
def give_sample_entry():
    conn, cursor = init_dbase()
    many_customers = [
                      ('bon', 'jovi', 'jovi@mew.com'),
                      ('scare', 'crow', 'crow@mew.com'),
                      ('meow', 'hulo', 'meow@mew.com'),
                      ('john', 'elder', 'john@mew.com'),
                      ('tim', 'smith', 'tim@mew.com'),
                      ('mary', 'brown', 'mary@mew.com')
                      ]
    cursor.executemany('''INSERT INTO customers VALUES (?, ?, ?)''', many_customers)
    conn.commit()
    conn.close()
    

# query the db and return all records
def show_all():
    conn, cursor = init_dbase()
    # define the query statement
    statement = """SELECT rowid, * FROM customers"""
    # execute the statement
    cursor.execute(statement)
    # fetch all
    items = cursor.fetchall()
    for item in items:
        print(item)
    # commit the command
    conn.commit()
    # close connection
    conn.close()

# add a new record to the table
def add_one(first_name, last_name, email):
    conn, cursor = init_dbase()
    cursor.execute("INSERT INTO customers VALUES (?, ?, ?)", (first_name, last_name, email))
    conn.commit()
    conn.close()

# delete a record from the table
def delete_one(id):
    conn, cursor = init_dbase()
    cursor.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()

# add many records to the table
def add_many(list):
    conn, cursor = init_dbase()
    cursor.executemany("INSERT INTO customers VALUES (?, ?, ?)", (list))
    conn.commit()
    conn.cursor()

# lookup with where
def email_lookup(email):
    conn, cursor = init_dbase()
    cursor.execute("SELECT rowid, * from customers WHERE email = (?)", (email, ))
    items = cursor.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()