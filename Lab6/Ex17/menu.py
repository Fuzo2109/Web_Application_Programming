from flask import Flask, render_template, abort

app = Flask(__name__)

menu_data ={
    "drinks":[
        {"name": "Coffee", "price": 2.5},
        {"name": "Tea", "price": 2.0},
        {"name": "Juice", "price": 3.0}
    ],
    "food":[
        {"name": "Sandwich", "price": 5.0},
        {"name": "Salad", "price": 4.5},
        {"name": "Soup", "price": 3.5}
    ]
}

@app.route("/menu/<category>")
def menu(category):
    if category not in menu_data:
        return "<h1> 404 - Category Not Found</h1>", 404
    items = menu_data[category]
    return render_template("menu.html", category=category.title(), items=items)

if __name__ == "__main__":
    app.run(debug=True)