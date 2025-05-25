from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def student_info():
    student = {
        'name': 'Phu',
        'student_id': '2374802010390',
        'academic_year': '2023-2027',
        'major': 'Information Technology',
        'hobbies': 'Reading, Swimming, Coding'
    }
    return render_template('index.html', student=student)

if __name__ == '__main__':
    app.run(debug=True, port=5003)