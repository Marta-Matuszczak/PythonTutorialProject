import sqlite3

with sqlite3.connect("simple.db") as db:
    cursor = db.cursor()

    # wyświetli zawartość całej tabeli scores
    cursor.execute('''
        select * from scores
    ''')

    rows = cursor.fetchall()
    for r in rows:
        print(r[1], r[2], r[3])

    cursor.execute('''
        select count(*) from scores
    ''')

    rows = cursor.fetchone()
    print("Rows:", rows[0])
