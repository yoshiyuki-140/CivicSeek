import sqlite3

dbname = "exampledb"

conn = sqlite3.connect(dbname)


cursole = conn.cursor()

# テーブルの作成
cursole.execute(
    "create table persons(id integer primary key autoincrement, name string)"
)
conn.commit()


cursole.close()
conn.close()
