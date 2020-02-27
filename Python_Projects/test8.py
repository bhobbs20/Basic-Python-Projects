import _sqlite3

conn = _sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()


conn = _sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Mike', 'Captain', 'thecapt@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Kevin', 'Bacon', 'baconk@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Todd', 'Fertil', 'thetoddh@gmail.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) VALUES (?, ?, ?)", \
                ('Pascal', 'Hobbs', 'impascal@gmail.com'))
    conn.commit()
conn.close()

conn = _sqlite3.connect('test.db')
with conn:
    curr = conn.cursor()
    curr.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons WHERE col_fname = 'Pascal' ")
    var_person = curr.fetchall()
    for item in var_person:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0], item[1], item[2])
    print(msg)
    conn.commit()
conn.close()