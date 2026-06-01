from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    universities = []

    if request.method == "POST":

        cgpa = float(request.form["cgpa"])
        ielts = float(request.form["ielts"])
        budget = int(request.form["budget"])

        df = pd.read_csv("universities.csv")

        result = df[
            (df["Min_CGPA"] <= cgpa) &
            (df["Min_IELTS"] <= ielts) &
            (df["Max_Budget"] <= budget)
        ]

        universities = result.to_dict("records")

    return render_template(
        "index.html",
        universities=universities
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)