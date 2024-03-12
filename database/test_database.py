from typing import Optional
import unittest
import mysql.connector

def connect_to_mysql(database: Optional[str] = None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Drakonas24!",
        database=database
    )
    return mydb

class TestDatabaseOperations(unittest.TestCase):

    def setUp(self):
        database_connection = connect_to_mysql()
        cursor = database_connection.cursor()
        cursor.execute("""CREATE DATABASE IF NOT EXISTS test_database;""")
        cursor.close()
        
        database_connection = connect_to_mysql(database='test_database')
        cursor = database_connection.cursor()
        cursor.execute(
        """
            CREATE TABLE User (
                id INT AUTO_INCREMENT PRIMARY KEY, 
                full_name VARCHAR(255)
            );
            CREATE TABLE Quiz (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                ongoing bool,
                user_id INT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User(id)
            );
            CREATE TABLE Question (
                id INT AUTO_INCREMENT PRIMARY KEY,
                question VARCHAR(255),
                quiz_id INT NOT NULL,
                FOREIGN KEY (quiz_id) REFERENCES Quiz(id)
            );
            CREATE TABLE Answer (
                id INT AUTO_INCREMENT PRIMARY KEY,
                answer VARCHAR(255),
                question_id INT NOT NULL,
                FOREIGN KEY (question_id) REFERENCES Question(id)
            );
        """
        ) 
        cursor.close()
        

    def test_add_and_retrieve_user(self):
        database_connection = connect_to_mysql(database='test_database')
        cursor = database_connection.cursor()
        cursor.executemany("""
            INSERT INTO User(id, full_name) VALUES (%s, %s);
        """,
            [(1, 'John Doe'), (2, 'John Doe Second'), (3, 'John Doe Third')]
        )
        database_connection.commit()
        cursor.close()

        database_connection = connect_to_mysql(database='test_database')
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM User;")
        users = cursor.fetchall()
        cursor.close()

        assert users == [(1, 'John Doe'), (2, 'John Doe Second'), (3, 'John Doe Third')]

    def test_add_and_retrieve_quizzes_for_a_user(self):

        database_connection = connect_to_mysql(database='test_database')
        cursor = database_connection.cursor()
        cursor.executemany("""
            INSERT INTO User(id, full_name) VALUES (%s, %s);
        """,
            [(1, 'John Doe'), (2, 'John Doe Second'), (3, 'John Doe Third')]
        )
        database_connection.commit()
        cursor.close()

        database_connection = connect_to_mysql(database='test_database')
        cursor = database_connection.cursor()
        cursor.executemany("""
            INSERT INTO Quiz(id, name, ongoing, user_id) VALUES (%s, %s, %s, %s);
        """,
            [(1, "Quiz1", False, 2), (2, "Quiz2", False, 2), (3, "Quiz3", False, 3)]
        )
        database_connection.commit()
        cursor.close()

        database_connection = connect_to_mysql(database='test_database')
        cursor = database_connection.cursor()
        cursor.execute("SELECT * FROM Quiz WHERE user_id = 2")
        quizzes = cursor.fetchall()
        cursor.close()

        assert quizzes == [(1, "Quiz1", False, 2), (2, "Quiz2", False, 2)]

    def tearDown(self) -> None:
        database_connection = connect_to_mysql()
        cursor = database_connection.cursor()
        cursor.execute("DROP DATABASE test_database;")
        cursor.close()

unittest.main()
