from flask import Flask, render_template, abort

app = Flask(__name__)

faqs = {
    1: {
        "question": "What is Flask?",
        "answer": "Flask is a micro web framework for Python based on Werkzeug and Jinja2."
    },
    2: {
        "question": "How do I install Flask?",
        "answer": "You can install Flask using pip: `pip install Flask`."
    }
}

@app.route("/faq/<int:question_id>")
def show_faq(question_id):
    faq = faqs.get(question_id)
    if not faq:
        return "<h1>404 - FAQ Not Found</h1>", 404
    return render_template("faq.html", faq=faq)

if __name__ == "__main__":
    app.run(debug=True)