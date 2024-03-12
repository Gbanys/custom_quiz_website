from typing import Optional
import mysql.connector

def connect_to_mysql(database: Optional[str] = None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database=database
    )
    return mydb


def create_local_mysql_database_and_tables():
    database_connection = connect_to_mysql()
    cursor = database_connection.cursor()
    cursor.execute("""CREATE DATABASE IF NOT EXISTS quiz_database;""")
    cursor.close()

    database_connection = connect_to_mysql(database='quiz_database')
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
            answered_correctly BOOL,
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


def add_user(id: Optional[int], full_name: str) -> None:
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.executemany("""
        INSERT INTO User(id, full_name) VALUES (%s, %s);
    """,
        [(id, full_name)]
    )
    database_connection.commit()
    cursor.close()


def get_quizzes_from_user(user_id: int):
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute(f"SELECT * FROM Quiz WHERE user_id = {user_id}")
    quizzes = cursor.fetchall()
    cursor.close()
    return quizzes

def get_single_quiz(quiz_id: int):
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute(f"SELECT * FROM Quiz WHERE id = {quiz_id}")
    quiz = cursor.fetchall()
    cursor.close()
    return quiz
    

def get_questions_from_quiz(quiz_id: int):
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute(f"SELECT * FROM Question WHERE quiz_id = {quiz_id}")
    questions = cursor.fetchall()
    cursor.close()
    return questions

def get_first_unanswered_question(quiz_id: int):
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute(f"SELECT * FROM Question WHERE quiz_id = {quiz_id} AND answered_correctly IS NULL ORDER BY id ASC LIMIT 1;")
    questions = cursor.fetchall()
    cursor.close()
    return questions

def get_answers_from_question(question_id: int):
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute(f"SELECT * FROM Answer WHERE question_id = {question_id}")
    answers = cursor.fetchall()
    cursor.close()
    return answers

def get_all_answers():
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute("SELECT * FROM Answer")
    answers = cursor.fetchall()
    cursor.close()
    return answers

def update_question_status(question_id: int, answered_correctly: bool):
    database_connection = connect_to_mysql(database='quiz_database')
    cursor = database_connection.cursor()
    cursor.execute(f"UPDATE Question SET answered_correctly = {answered_correctly} WHERE id = {question_id}")
    cursor.close()
    database_connection.commit()
