import sqlite3
from pprint import pprint

DB_PATH = 'my_first_db.sqlite3'

with sqlite3.connect(DB_PATH) as connection:
    cursor = connection.cursor()

    # Creating table

    query = """
        CREATE TABLE IF NOT EXISTS schools(
             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            school_number INTEGER NOT NULL,
            address TEXT NOT NULL,
            floors INTEGER NOT NULL CHECK(floors >= 1)

        )
    """
    cursor.execute(query)

    query = """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            surname TEXT NOT NULL,
            name TEXT NOT NULL,
            specialization TEXT,
            school_id INTEGER,
            FOREIGN KEY (school_id) REFERENCES schools(id)
    
        )
    """
    cursor.execute(query)

    # dynamic data

    # school_number = 51
    # address = 'Philipp Orlik 13'
    # floors = 3
    # values = [school_number, address, floors]
    #
    # query = """
    #     INSERT INTO schools(school_number, address, floors)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # school_number = 109
    # address = 'Panasa Mirnogo 92'
    # floors = 4
    # values = [school_number, address, floors]
    #
    # query = """
    #     INSERT INTO schools(school_number, address, floors)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # school_number = 19
    # address = 'Panasa Mirnaya 1488'
    # floors = 2
    # values = [school_number, address, floors]
    #
    # query = """
    #     INSERT INTO schools(school_number, address, floors)
    #     VALUES (?, ?, ?)
    # """
    # cursor.execute(query, values)

    # students = [
    #     ('Ivanov', 'Ivan', 'Math', 1),
    #     ('Petrov', 'Petr', 'Physics', 2),
    #     ('Sidorov', 'Sidr', 'Chemistry', 3),
    #     ('Kuznetsov', 'Kuzma', 'Biology', 1),
    #     ('Nikolaev', 'Nikolai', 'Geography', 2),
    #     ('Fedorov', 'Fedor', 'History', 3),
    #     ('Sergeev', 'Sergei', 'Math', 1),
    #     ('Alexeev', 'Alexey', 'Physics', 2),
    #     ('Dmitriev', 'Dmitry', 'Chemistry', 3),
    #     ('Andreev', 'Andrey', 'Biology', 1)
    # ]
    #
    # query = """
    #     INSERT INTO students(surname, name, specialization, school_id)
    #     VALUES (?, ?, ?, ?)
    # """
    #
    # cursor.executemany(query, students)
    #
    # query = """
    #     SELECT *
    #     FROM students
    #     JOIN schools ON students.school_id = schools.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())
    # *(*I*((*(*(*(*(*(*(*(*(*(*(

    # NEW HOMEWORK

    # query = """
    #     SELECT *
    #     FROM students
    #     LEFT JOIN schools
    #     ON students.school_id = schools.id
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    # query = """
    #     ALTER TABLE students
    #     ADD COLUMN phone_number TEXT
    #
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    # query = """
    #     UPDATE students
    #     SET
    #         phone_number = 38099659418
    #     WHERE id = 5
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())


    # query = """
    #     DELETE
    #     FROM students
    #     WHERE students.id BETWEEN 2 AND 4
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())

    # query = """
    #     SELECT *
    #     FROM students
    #     ORDER BY students.id DESC
    #     LIMIT 3
    #     OFFSET 2
    #
    # """
    # result = cursor.execute(query)
    # pprint(result.fetchall())
