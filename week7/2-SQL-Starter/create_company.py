import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT, monthly_salary FLOAT,
                   yearly_bonus FLOAT, position TEXT)
"""
insert_users_table = [
    "INSERT INTO users(name, monthly_salary, yearly_bonus, position) values('Ivan Ivanov', 5000, 10000, 'Software Developer');",
    "INSERT INTO users(name, monthly_salary, yearly_bonus, position) values('Rado Rado', 500, 0, 'Technical Support Intern');",
    "INSERT INTO users(name, monthly_salary, yearly_bonus, position) values('Ivo Ivo', 10000, 100000, 'CEO');",
    "INSERT INTO users(name, monthly_salary, yearly_bonus, position) values('Petar Petrov', 3000, 1000, 'Marketing Manager');",
    "INSERT INTO users(name, monthly_salary, yearly_bonus, position) values('Maria Georgieva', 8000, 10000, 'COO');"]

cursor.execute(create_table_query)
for user in insert_users_table:
    cursor.execute(user)
conn.commit()
conn.close()
