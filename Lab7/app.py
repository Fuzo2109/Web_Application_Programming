from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["LAB7_MONGODB"]
collection = db["students"]

@app.route("/")
def index():
    students = list(collection.find())
    return render_template("index.html", students=students)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        student = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "major": request.form["major"]
        }
        collection.insert_one(student)
        return redirect(url_for("index"))
    return render_template("form.html", student=None)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        update_fields = {
            "name": request.form["name"],
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "major": request.form["major"]
        }
        collection.update_one({"_id": ObjectId(id)}, {"$set": update_fields})
        return redirect(url_for("index"))
    return render_template("form.html", student=student)

@app.route("/delete/<id>")
def delete(id):
    collection.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("index"))

@app.route("/search")
def search():
    name = request.args.get("name")
    students = list(collection.find({"name": name}))
    return render_template("index.html", students=students)

@app.route("/fuzzy")
def fuzzy():
    keyword = request.args.get("q")
    students = list(collection.find({"name": {"$regex": keyword, "$options": "i"}}))
    return render_template("index.html", students=students)

@app.route("/filter/major")
def filter_major():
    major = request.args.get("major")
    students = list(collection.find({"major": major}))
    return render_template("index.html", students=students)

@app.route("/count-major")
def count_by_major():
    pipeline = [
        {"$group": {"_id": "$major", "count": {"$sum": 1}}}
    ]
    stats = list(collection.aggregate(pipeline))
    return render_template("count.html", stats=stats)

@app.route("/edit-scores/<id>", methods=["GET", "POST"])
def edit_scores(id):
    student = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        update_fields = {
            "math": float(request.form["math"]),
            "literature": float(request.form["literature"]),
            "english": float(request.form["english"])
        }
        collection.update_one({"_id": ObjectId(id)}, {"$set": update_fields})
        return redirect(url_for("index"))
    return render_template("form_scores.html", student=student)

@app.route("/calculate-gpa")
def calculate_gpa():
    students = collection.find()
    for s in students:
        if all(sub in s for sub in ["math", "literature", "english"]):
            gpa = (s["math"] + s["literature"] + s["english"]) / 3
            collection.update_one({"_id": s["_id"]}, {"$set": {"gpa": round(gpa, 2)}})
    return redirect(url_for("index"))

@app.route("/classify")
def classify():
    students = collection.find()
    for s in students:
        if "gpa" in s:
            rank = "Average"
            if s["gpa"] >= 8:
                rank = "Excellent"
            elif s["gpa"] >= 6.5:
                rank = "Good"
            collection.update_one({"_id": s["_id"]}, {"$set": {"rank": rank}})
    return redirect(url_for("index"))

@app.route("/excellent")
def filter_excellent():
    students = list(collection.find({"gpa": {"$gte": 8}}))
    return render_template("index.html", students=students)

@app.route("/top-student")
def top_student():
    student = collection.find_one(sort=[("gpa", -1)])
    return render_template("top.html", student=student)

@app.route("/age-range")
def age_range():
    min_age = int(request.args.get("min"))
    max_age = int(request.args.get("max"))
    students = list(collection.find({"age": {"$gte": min_age, "$lte": max_age}}))
    return render_template("index.html", students=students)

@app.route("/gender")
def filter_gender():
    gender = request.args.get("gender")
    students = list(collection.find({"gender": gender}))
    return render_template("index.html", students=students)

if __name__ == '__main__':
    app.run(debug=True)