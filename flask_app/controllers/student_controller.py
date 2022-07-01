from flask import session, render_template, request, redirect, flash
from flask_app import app

from flask_app.models.student_model import Student

@app.route('/')
def display_home():
    return render_template("index.html")

@app.route('/students')
def display_students():
    students = Student.get_all_students()
    return render_template("students.html", students = students)

@app.route('/students/<name>')
def show_single_student(name):
    data = {
        'name': name
    }
    student = Student.display_student(data)
    return render_template("student_profile.html", student = student)

@app.route('/quiz')
def display_quiz():
    return render_template("quiz.html")

@app.route('/quiz/submit', methods=['POST'])
def quiz_submit():
    Student.validate_quiz(request.form)
    return redirect('/quiz')