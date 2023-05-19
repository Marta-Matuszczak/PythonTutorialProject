import sqlite3

db = sqlite3.connect("simple.db")  # if database does not exist, it will be created
cursor = db.cursor()  # za pomocą kursora można się odnosić do bazy danych i wykonywać różne polecenia

# przekazujemy zapytanie SQL - tworzymy tabelę o nazwie scores
cursor.execute('''
    CREATE TABLE scores (
        id integer,
        name string,
        surname string,
        score integer)
''')

db.commit()  # zapisujemy zmiany w bazie
db.close()  # zamykamy bazę
