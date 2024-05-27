import sqlite3 as sql
import dBase as db

# db.create_table()
# db.give_sample_entry()
# db.add_one("thomas", "adison", "edison@meow.com")
# db.delete_one('7') # use rowid as string
# stuff = [
#     ("brenda", "smith", "smith@mew.com"),
#     ("jacob", "ramsey", "ramsey@mew.com")
# ]
# db.add_many(stuff)
db.email_lookup("mary@mew.com")
# db.show_all()