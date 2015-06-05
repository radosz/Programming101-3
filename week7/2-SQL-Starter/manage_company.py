import sqlite3
from tabulate import tabulate

conn = sqlite3.connect("company.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


list_employees_q = """SELECT name,position
FROM users"""

monthly_spending_q = """SELECT SUM(monthly_salary) as MONTHLY_SPENDING
FROM users"""

yearly_spending_q = """
SELECT SUM(yearly_bonus+monthly_salary) as YEARLY_SPENDING
FROM users
"""
add_employee_q = """INSERT INTO users(name, monthly_salary, yearly_bonus, position)
values(?, ?, ?, ?)
"""
delete_employee_q = """DELETE FROM users WHERE id = ?
"""
update_employee_q = """UPDATE users
SET name = ?,monthly_salary = ?,yearly_bonus = ?,position = ?
WHERE id = ?;"""

name_q = """SELECT name FROM users WHERE id = ?"""


def list_employees():
    table = []
    head = ["name", "position"]
    for row in cursor.execute(list_employees_q):
        rows = [row[x] for x in head]
        table.append(rows)
    return tabulate(table, headers=head, tablefmt="rst")


def monthly_spending():
    spending = cursor.execute(
        monthly_spending_q).fetchone()["MONTHLY_SPENDING"]
    return "The company is spending {} every month!".format(spending)


def yearly_spending():
    spending = cursor.execute(yearly_spending_q).fetchone()["YEARLY_SPENDING"]
    return "The company is spending {} every year!".format(spending)


def delete_employee(id):
    e_name = name(id)
    cursor.execute(delete_employee_q, (id,))
    conn.commit()
    return "{} was a deleted".format(e_name)


def update_employee(id, name, monthly_salary, yearly_bonus, position):
    cursor.execute(
        update_employee_q, (name, monthly_salary, yearly_bonus, position, id))
    conn.commit()


def name(id):
    return cursor.execute(name_q, (id,)).fetchone()["name"]
