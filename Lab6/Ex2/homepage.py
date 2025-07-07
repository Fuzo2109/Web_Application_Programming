from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/about")
def about():
    return "<h1>About Page</h1><p>This is the about page of our Flask app.</p>"

if __name__== "__main__":
    app.run(debug=True)
