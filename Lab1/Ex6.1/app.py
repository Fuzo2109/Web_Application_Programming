from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def linear_equation():
    x = -2
    y = 5 * x + 7
    return render_template('index.html', x=x, y=y)

if __name__ == '__main__':
    app.run(debug=True)