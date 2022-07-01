from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import database
from flask import flash, session


class Student:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.real_name = data['real_name']
        self.quirk = data['quirk']
        self.quirk_description = data['quirk_description']
        self.description = data['description']
        self.birthday = data['birthday']
        self.age = data['age']
        self.height = data['height']
        self.favorite_food = data['favorite_food']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.hero_id = data['hero_id']


    @classmethod
    def get_all_students(cls):
        query = 'SELECT * FROM students;'
        results = connectToMySQL(database).query_db(query)

        list_students = []

        if len(results) > 0:
            for student in results:
                list_students.append(cls(student))
        return list_students

    @classmethod
    def display_student(cls, data):
        query = "SELECT * FROM students LEFT JOIN heroes ON heroes.id = students.hero_id WHERE students.name = %(name)s;"
        single_result = connectToMySQL(database).query_db(query, data)[0]
        student = cls(single_result)
        student.mentor_name = single_result["heroes.name"]

        return student

    @staticmethod
    def validate_quiz(data):
        if len(data['question_1']) < 1:
            flash("Come on, at least try to answer the question!", "answer_question_1")
        elif data['question_1'] == "Minoru Mineta" or data['question_1'] == "Mineta" or data['question_1'] == "Grape Juice":
            flash("Hey, you got it right!", "answer_question_1")
        else:
            flash("Not quite right!", "answer_question_1")

        if len(data['question_2']) < 1:
            flash("Come on, at least try to answer the question!", "answer_question_2")
        elif data['question_2'] == "Foldabody":
            flash("Hey, you got it right!", "answer_question_2")
        else:
            flash("Not quite right!", "answer_question_2")

        if len(data['question_3']) < 1:
            flash("Come on, at least try to answer the question!", "answer_question_3")
        elif data['question_3'] == "32":
            flash("Hey, you got it right!", "answer_question_3")
        else:
            flash("Not quite right!", "answer_question_3")

        if len(data['question_4']) < 1:
            flash("Come on, at least try to answer the question!", "answer_question_4")
        elif data['question_4'] == "Ingenium" or data['question_4'] == "Tenya Iida" or data['question_4'] == "Iida":
            flash("Hey, you got it right!", "answer_question_4")
        else:
            flash("Not quite right!", "answer_question_4")

        if len(data['question_5']) < 1:
            flash("Come on, at least try to answer the question!", "answer_question_5")
        elif data['question_5'] == "Anima" or data['question_5'] == "Koji Koda" or data['question_5'] == "Koda":
            flash("Hey, you got it right!", "answer_question_5")
        else:
            flash("Not quite right!", "answer_question_5")