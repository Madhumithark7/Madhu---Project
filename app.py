from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("universities.csv")


# 🎯 MATCH CALCULATION FUNCTION
def calculate_match(user, uni):
    match = 0

    match += max(0, 50 - abs(user["cgpa"] - uni["Min_CGPA"]) * 10)
    match += max(0, 30 - abs(user["ielts"] - uni["Min_IELTS"]) * 8)

    if user["budget"] >= uni["Tuition_Fee"]:
        match += 20
    else:
        match += 5

    match += (uni["Acceptance_Rate"] / 100) * 20
    match += max(0, (200 - uni["World_Ranking"]) / 10)

    match = max(0, min(100, match))
    return round(match, 1)


@app.route("/", methods=["GET", "POST"])
def home():

    results = []
    searched = False

    countries = df["Country"].unique()
    programs = df["Program"].unique()

    if request.method == "POST":
        searched = True

        user = {
            "cgpa": float(request.form["cgpa"]),
            "ielts": float(request.form["ielts"]),
            "budget": int(request.form["budget"]),
            "country": request.form.get("country"),
            "program": request.form.get("program")
        }

        data = df.copy()

        # 🌍 filters
        if user["country"] != "All":
            data = data[data["Country"] == user["country"]]

        if user["program"] != "All":
            data = data[data["Program"] == user["program"]]

        # 🚨 FIX: remove duplicates
        data = data.drop_duplicates(subset=["University", "Country", "Program"])

        # 🧠 keep only best match per university
        best_results = {}

        for _, uni in data.iterrows():
            match = calculate_match(user, uni)

            key = uni["University"]

            if key not in best_results or match > best_results[key]["match"]:

                if match >= 75:
                    level = "🎯 Dream Match"
                elif match >= 50:
                    level = "👍 Good Match"
                else:
                    level = "🟢 Possible Match"

                best_results[key] = {
                    "name": uni["University"],
                    "country": uni["Country"],
                    "program": uni["Program"],
                    "match": match,
                    "level": level,
                    "ranking": uni["World_Ranking"],
                    "job": uni["Job_Prospect"]
                }

        # sort results
        results = sorted(best_results.values(), key=lambda x: x["match"], reverse=True)

    return render_template(
        "index.html",
        results=results,
        countries=countries,
        programs=programs,
        searched=searched
    )


if __name__ == "__main__":
    app.run(debug=True)