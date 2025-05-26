from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        gender = request.form['gender']
        membership = request.form['membership']
        color = request.form['favcolor']
        is_correct = 'correct' in request.form
        flash('Student Information Submmited Successfully!', 'success')

        return f"Submited : {username}, {gender}, {membership}, {color}, Correct: {is_correct}"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)