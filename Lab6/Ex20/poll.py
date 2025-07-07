from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

votes ={
   "Lions": 0,
    "Tigers": 0
}

@app.route("/poll", methods=["GET", "POST"])
def poll():
    if request.method == "POST":
        option = request.form.get("animal")
        if option in votes:
            votes[option] += 1
        return redirect(url_for("poll"))

    total_votes = sum(votes.values())

    results = []
    for animal, count in votes.items():
        percentage = (count/total_votes) * 100 if total_votes > 0 else 0
        results.append({"option": animal, "count": count, "percentage": round(percentage, 2)})

    return render_template("poll.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)