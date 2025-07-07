from flask import Flask, render_template, abort

app = Flask(__name__)

posts ={
    1:{"title": "First Post", "content": "Hello, world!"},
    2: {"title": "Second Post", "content": "Flask is great!"},
    3: {"title": "Third Post", "content": "You are a good  person!"}
}

@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts.get(post_id)
    if post is None:
        return "<h1> 404 - Post Not Found</h1>", 404
    return render_template("blog.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)