import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()
# c.execute("""CREATE TABLE user(
#            name text,
#           email text,
#            password text
# )""")

#c.execute("INSERT INTO user VALUES ('saad', 'ahmad.saad2636@gmail.com', 'madwalker')")
#conn.commit()
#c.execute("INSERT INTO user VALUES ('taki', 'sarwar.taki@gmail.com', 'aniqartaki')")
#conn.commit()
c.execute("DELETE FROM user where name='taki'")
conn.commit()
c.execute("SELECT * FROM user where name='taki'")

print(c.fetchmany())
conn.commit()

conn.close()
