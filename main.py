import sqlite3

conn = sqlite3.connect('./db.sqlite3')


sql = ''' INSERT INTO game_signin(username,password)
              VALUES('Sai','123456') '''
# cur = conn.cursor()
# cur.execute(sql)
# conn.commit()
# data = conn.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
# data = conn.execute('select * from game_signup').fetchall()
username = 'Yeshwanth'
email = conn.execute(f"select email from game_signup where username='{username}';").fetchall()
print(email[0][0])
