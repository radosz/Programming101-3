import requests
import sqlite3

create_table_students = """CREATE TABLE IF NOT EXISTS students(
student_id INTEGER PRIMARY KEY,
name TEXT,
github TEXT)
"""

create_table_course = """CREATE TABLE IF NOT EXISTS courses(
course_id INTEGER PRIMARY KEY, name TEXT)
"""

create_realatino_table = """CREATE TABLE IF NOT EXISTS relation(
student_id INTEGER,
course_id INTEGER,
FOREIGN KEY(student_id) REFERENCES students(student_id),
FOREIGN KEY(course_id) REFERENCES courses(course_id))"""

insert_into_query = """INSERT INTO {} ("{}")
VALUES ("{}")
"""
insert_into_students = """INSERT INTO students ('student_id','name','github') VALUES ('{}','{}','{}')
"""
insert_into_relation = """INSERT INTO relation('student_id','course_id') VALUES ('{}','{}')
"""


class LastHR:

    def __init__(self, database_name):
        self.connect = sqlite3.connect(database_name)
        self.connect.row_factory = sqlite3.Row
        self.db = self.connect.cursor()
        self.json = self.connect_to_hackbg_api()

    def get_courses(self):
        courses = []
        for element in self.json:
            try:
                course_name = element["courses"][0]["name"]
                courses.append(course_name)
            except IndexError:
                pass
        courses = list(set(courses))
        courses.sort()
        return courses

    def course_id_dict(self):
        courses = self.get_courses()
        course_id = {}
        id = 0
        for course in courses:
            id += 1
            course_id[course] = id
        return course_id

    def get_students(self):
        students = []
        id = 0
        for element in self.json:
            try:
                id += 1
                student_name = element["name"]
                github = element["github"]
                students.append(
                    (id, student_name, github, [x["name"] for x in element["courses"]]))
            except IndexError:
                pass
        return students

    def courses_table(self):
        self.db.execute(create_table_course)
        for course in self.get_courses():
            self.db.execute(
                insert_into_query.format("courses", "name", course))
        self.connect.commit()

    def relation_table(self):
        self.db.execute(create_realatino_table)
        course_d = self.course_id_dict()
        for student in self.get_students():
            s_id, name, github, courses = student
            for course in courses:
                try:
                    self.db.execute(
                        insert_into_relation.format(s_id, course_d[course]))
                except IndexError:
                    pass
        self.connect.commit()

    def students_table(self):
        self.db.execute(create_table_students)
        for student in self.get_students():
            id, name, github, course = student
            self.db.execute(
                insert_into_students.format(id, name, github))
        self.connect.commit()

    def top_students(self):
        count_course = []
        student_names = []
        ids = []
        course_s = {}
        top = ""
        for student in self.get_students():
            s_id, name, github, courses = student
            count_course.append(len(courses))
            ids.append(s_id)
            course_s[s_id] = courses
            student_names.append(name)
        count, student, id_s = zip(
            *sorted(zip(count_course, student_names, ids)))
        for n, c, s_id in zip(reversed(student), reversed(count), reversed(id_s)):
            if c != 0:
                top += "{}{}{} {}\n".format(n, "." *
                                            (35 - len(n)), c, course_s[s_id])
        return top

    def rating_to_file(self):
        with open("rating.txt", "w") as top:
            top.write(self.top_students())
            top.close()

    def connect_to_hackbg_api(self):
        r = requests.get("https://hackbulgaria.com/api/students/")
        return r.json()

    def create_all_tables(self):
        self.students_table()
        self.courses_table()
        self.relation_table()


def main():
    lhr = LastHR("hackbg.db")
    lhr.rating_to_file()
    lhr.create_all_tables()

if __name__ == '__main__':
    main()
