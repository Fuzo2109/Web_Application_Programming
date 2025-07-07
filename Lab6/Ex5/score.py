from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        physics = request.form['physics']
        chemistry = request.form['chemistry']
        maths = request.form['maths']
        return render_template('result.html', name=name, physics=physics, chemistry=chemistry, maths=maths)
    return render_template('score.html')

if __name__ == '__main__':
    app.run(debug=True)