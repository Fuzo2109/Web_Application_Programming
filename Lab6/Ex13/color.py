from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/color", methods=["GET", "POST"])
def color_changer():
    color = "white"
    if request.method == "POST":
        user_color = request.form.get("color")
        if user_color:
            color = user_color
    return render_template("color.html", color=color) 

if __name__ == "__main__":
    app.run(debug=True)
