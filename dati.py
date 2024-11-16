import sqlite3


conn = sqlite3.connect("dati.db", check_same_thread=False)

def lietotaju_tabulu_izveide():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE lietotaji(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        vards TEXT not NULL,
        uzvards TEXT not NULL,
        lietotajvards TEXT not NULL
        )
        """
    )
    conn.commit()


# lietotaju_tabulu_izveide()

def pievienot_lietotaju(vards, uzvards, lietotajvards):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO lietotaji(vards, uzvards, lietotajvards) VALUES("{vards}","{uzvards}","{lietotajvards}")
        """
    )
    conn.commit()
