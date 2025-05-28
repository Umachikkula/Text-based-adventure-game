import sqlite3

def save_to_db(a, op, b, result):
    conn = sqlite3.connect("reports/history.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS operations
                 (a REAL, op TEXT, b REAL, result REAL)''')
    c.execute("INSERT INTO operations VALUES (?, ?, ?, ?)", (a, op, b, result))
    conn.commit()
    conn.close()
