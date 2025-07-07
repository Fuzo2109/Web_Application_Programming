from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/convert", methods=["GET", "POST"])
def convert_temperature():
    result = None
    if request.method == "POST":
        try:
            temp = float(request.form["temperature"])
            conversion_type = request.form["conversion"]
            if conversion_type == "c_to_f":
                result = f"{temp}°C = {round((temp * 9/5) +32, 2)}°F"
            elif conversion_type == "f_to_c":
                result = f"{temp}°F = {round((temp - 32) * 5/9, 2)}°C"
        except ValueError:
            result = "Invaild temperature input!"
    return render_template("temperature.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)