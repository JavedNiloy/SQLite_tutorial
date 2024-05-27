import sqlite3 as sql

# connect to database
conn = sql.connect('customer.db')

# create a cursor
c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE customers (
#           first_name text,
#           last_name text,
#           email text
#     )""")

# # Many entry
# many_customers = [
#                   ('bon', 'jovi', 'jovi@mew.com'),
#                   ('scare', 'crow', 'crow@mew.com'),
#                   ('meow', 'hulo', 'meow@mew.com')
#                   ]


# # Insert into the table
# c.execute('''INSERT INTO customers VALUES ('john', 'elder', 'john@mew.com')''')
# c.execute('''INSERT INTO customers VALUES ('tim', 'smith', 'tim@mew.com')''')
# c.execute('''INSERT INTO customers VALUES ('mary', 'brown', 'mary@mew.com')''')

# # Execute many
# c.executemany('''INSERT INTO customers VALUES (?, ?, ?)''', many_customers)


# DATATYPES: NULL, INTEGER, TEXT, BLOB

# Update records
# c.execute("""UPDATE customers SET first_name = 'bob'
#             WHERE last_name = 'elder'
#     """)
# c.execute("""UPDATE customers SET first_name = 'john'
#             WHERE rowid = 1
#     """)

# # Delete records
# c.execute("DELETE from customers WHERE rowid = 6")

# conn.commit()

# Query the Database
# c.execute("""SELECT * FROM customers""")
# c.execute("""SELECT rowid, * FROM customers""")
# c.execute("SELECT rowid, * FROM customers WHERE last_name = 'brown'")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Cr%'")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%ow%'")
# c.fetchone()
# c.fetchmany(3)
# items = c.fetchall()
# print("NAME" + "\t\t\tEMAIL")
# print("------" + "\t\t\t-------------")
# for item in items:
#     print(item[0] + " " + item[1] + "\t\t" + item[2])
# for item in items:
#     print(item)

# Query the database -- order by
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name")

# Query the database -- and/or
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%ow%' AND rowid = 3")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%ow%' OR rowid = 11")
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%ow%' OR first_name LIKE 't%'")

# Query the database -- limit result
# c.execute("SELECT rowid, * FROM customers LIMIT 5")
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 5")

# items = c.fetchall()
# for item in items:
#     print(item)

# print("Command executed successfully .....")

# Drop table
c.execute("DROP TABLE customers")

# Commit our command
conn.commit()

c.execute("SELECT rowid, * FROM customers")
items = c.fetchall()
for item in items:
    print(item)

# Close our connection
conn.close()