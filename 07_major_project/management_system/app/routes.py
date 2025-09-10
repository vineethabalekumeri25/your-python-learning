from flask import render_template, request, redirect, flash
from . import db
from .models import Student
from flask import current_app as app

@app.route("/")
def index():
    students = Student.query.all()
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        if not name or not email or not course:
            flash("All fields are required!", "error")
            return redirect("/add")

        student = Student(name=name, email=email, course=course)
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully!", "success")
        return redirect("/")
    return render_template("add_record.html")

@app.route("/delete/<int:id>")
def delete_student(id):
    student = Student.query.get(id)
    if student:
        db.session.delete(student)
        db.session.commit()
        flash("Student deleted!", "success")
    return redirect("/")
