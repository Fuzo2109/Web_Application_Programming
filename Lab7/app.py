from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = "mongodb://localhost:27017/student_db"
db = client["students_db"]
collection = db["students"]

@app.route('/')
def index():
    students = list (collection.find())
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        major = request.form['major']
        list (collection.find())({'name': name, 'age': age, 'major': major})
        return redirect(url_for('index'))
    return render_template('form.html')

@app.route('/delete/<student_id>')
def delete_student(student_id):
    from bson.objectid import ObjectId
    list (collection.find())({'_id': ObjectId(student_id)})
    return redirect(url_for('index'))

@app.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    from bson.objectid import ObjectId
    student = list (collection.find())({'_id': ObjectId(student_id)})
    if request.method == 'POST':
        list (collection.find())({'_id': ObjectId(student_id)}, {'$set': {
            'name': request.form['name'],
            'age': request.form['age'],
            'major': request.form['major']
        }})
        return redirect(url_for('index'))
    return render_template('form.html', student=student)
    
if __name__ == '__main__':
    app.run(debug=True)
