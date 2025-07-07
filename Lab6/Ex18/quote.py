from flask import Flask, render_template
import random

app = Flask(__name__)

quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Cờ bạc người không chơi là người thắng, người chơi không bao giờ thắng - Huan Rose",
    "Life is what happens when you're busy making other plans. - John Lennon",
]

@app.route("/quote")
def quote():
    selected_quote = random.choice(quotes)
    return render_template("quote.html", quote=selected_quote)

if __name__ == "__main__":
    app.run(debug=True)