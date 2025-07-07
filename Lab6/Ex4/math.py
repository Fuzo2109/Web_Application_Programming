from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def square_page():
    num = request.args.get("num")
    if num:
        try:
            number = int(num)
            square = number ** 2
            return render_template("result.html", number=number, square=square)
        except ValueError:
            return "Invalid number!"
    return render_template("square.html")

if __name__ == "__main__":
    app.run(debug=True, port=5002)
