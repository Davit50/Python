import sqlite3 as sql
from pprint import pprint
con = sql.connect('data.db')
cur = con.cursor()

# cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, age INTEGER,name VARCHAR)')
# cur.execute("INSERT INTO categories(category) VALUES('water')")

# cur.execute("CREATE TABLE IF NOT EXISTS categories(id INTEGER PRIMARY KEY, category VARCHAR)")
# cur.execute("CREATE TABLE IF NOT EXISTS products(id INTEGER PRIMARY KEY, category_id VARCHAR, product VARCHAR)")

# cur.execute("INSERT INTO products(category_id,product) VALUES(2,'home')")

cur.execute("SELECT category, product FROM categories left join products ON categories.id =products.category_id")
# for i in cur:
#     if i[1] != None:
#         print(i)
data = dict()
for el in cur:
    if el[0] in data:
        data[el[0]].append(el[1])
    else:
        data[el[0]] = [el[1]]

con.commit()
cur.close()
con.close()
print(data)
