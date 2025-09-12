import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash
from app.models import Student, Course

app = Flask(__name__)
app.secret_key = "secret_key_for_flash_messages"

# Database connection
def get_db_connection():
    try:
        conn = sqlite3.connect('database.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection failed: {e}")
        return None

# Initialize database
def init_db():
    conn = get_db_connection()
    if conn:
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    course TEXT NOT NULL
                )
            ''')
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()

# Home - show students
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        students = conn.execute('SELECT * FROM students').fetchall()
        conn.close()
        return render_template('index.html', students=students)
    except Exception as e:
        flash(f"Error loading students: {e}")
        return render_template('index.html', students=[])

# Add new student
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        course_str = request.form.get('course')

        # Validate form input
        if not name or not email or not course_str:
            flash("All fields are required.")
            return redirect(url_for('add_student'))

        try:
            # Convert to Enum (ensures valid data)
            course = Course[course_str]

            # Use OOP class (Student) to hold data
            student = Student(name, email, course)

            conn = get_db_connection()
            conn.execute(
                'INSERT INTO students (name, email, course) VALUES (?, ?, ?)',
                (student.name, student.email, student.course.value)
            )
            conn.commit()
            conn.close()
            flash("Student added successfully!")
            return redirect(url_for('index'))
        except KeyError:
            flash("Invalid course selected.")
        except sqlite3.IntegrityError:
            flash("Email must be unique.")
        except Exception as e:
            flash(f"Error adding student: {e}")

    return render_template('add_student.html', courses=[c.name for c in Course])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
