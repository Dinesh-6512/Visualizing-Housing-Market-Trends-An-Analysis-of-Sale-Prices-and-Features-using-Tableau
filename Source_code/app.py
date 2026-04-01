from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    prediction = request.args.get("prediction")
    return render_template("index.html", prediction=prediction)


@app.route("/predict", methods=["POST"])
def predict():
    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    sqft = int(request.form["sqft"])

    predicted_price = (bedrooms * 50000) + (bathrooms * 30000) + (sqft * 100)

    # Redirect instead of returning template directly
    return redirect(url_for("index", prediction=predicted_price) + "#prediction")


if __name__ == "__main__":
    app.run(debug=True)
