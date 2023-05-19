import sqlite3
import random

with sqlite3.connect("simple.db") as db:
    cursor = db.cursor()
    names = ["A", "B", "C", "D", "E", "F"]
    surnames = ["x", "Y", "Z", "P", "Q", "L"]

    for i in range(6):
        name = random.choice(names)
        surname = random.choice(surnames)
        score = random.randint(0, 100)

        cursor.execute(f'''
            insert into scores (id, name, surname, score) values (
            {i}, "{name}", "{surname}", {score})
        ''')

    db.commit()
