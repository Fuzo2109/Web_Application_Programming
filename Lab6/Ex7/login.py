from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            message = "Login successful"
        else:
            message = "Login failed"

        return render_template("result.html", message=message)

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)