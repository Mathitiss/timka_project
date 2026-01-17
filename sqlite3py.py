import sqlite3

connection = sqlite3.connect('employees.db')
cursor = connection.cursor()

# cursor.execute("CREATE TABLE Employees(login, password)")
# cursor.execute("""
#     INSERT INTO Employees VALUES
#         ('Mathitiss', '12345')
# """)

# cursor.execute("DELETE FROM Employees")
# connection.commit()


cursor.execute("SELECT * FROM Employees")
database = dict()

for row in cursor.fetchall():
    key = row[0]
    value = row[1]

    database[key] = value

connection.close()