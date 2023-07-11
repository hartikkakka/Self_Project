import sqlite3


def connect():
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS employee_data (id INTEGER PRIMARY KEY, name TEXT, ctc INTEGER,"
                   "Ac_number INTEGER, IFSC TEXT)")

    conn.commit()
    conn.close()


def insert(name, ctc, Ac_number, IFSC):
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employee_data (name, ctc, Ac_number, IFSC) VALUES (?,?,?,?)", (name, ctc, Ac_number,
                                                                                               IFSC))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_data")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No records found.")
    return rows


def search(name):
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_data WHERE name=?", (name,))
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("No records found.")
    return rows


def delete(name):
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee_data WHERE name=?", (name,))
    conn.commit()
    conn.close()


def update(name, ctc, Ac_number, IFSC):
    conn = sqlite3.connect("employee_data.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE employee_data SET ctc=?, pl=?, Ac_number=?, IFSC=? WHERE name=?", (ctc, Ac_number, IFSC,
                                                                                              name))
    conn.commit()
    conn.close()
