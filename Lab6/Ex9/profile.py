from flask import Flask, render_template

app = Flask(__name__)

@app.route("/profile/<username>")
def profile(username):
    if username.lower() == "admin":
        message = "Hello Admin! You have special access!"
    else:
        message = f"Welcome to your profile, {username}!"
    return render_template("profile.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)