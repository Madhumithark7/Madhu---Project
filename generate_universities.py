import pandas as pd
import random

countries = {
    "USA": [
        "Harvard University", "MIT", "Stanford University", "UC Berkeley",
        "UCLA", "NYU", "Georgia Tech", "University of Washington",
        "Purdue University", "University of Michigan"
    ],
    "UK": [
        "University of Oxford", "University of Cambridge", "Imperial College London",
        "University College London", "University of Manchester",
        "University of Edinburgh", "King's College London",
        "University of Leeds", "University of Birmingham", "University of Glasgow"
    ],
    "Canada": [
        "University of Toronto", "University of British Columbia", "McGill University",
        "University of Alberta", "University of Waterloo", "McMaster University",
        "Western University", "University of Ottawa", "Queen's University",
        "Simon Fraser University"
    ],
    "Australia": [
        "University of Melbourne", "University of Sydney", "UNSW Sydney",
        "Monash University", "Australian National University",
        "University of Queensland", "University of Adelaide",
        "University of Western Australia", "RMIT University", "Macquarie University"
    ],
    "Germany": [
        "Technical University of Munich", "RWTH Aachen University",
        "Heidelberg University", "University of Freiburg",
        "University of Hamburg", "University of Stuttgart",
        "Free University of Berlin", "University of Cologne",
        "TU Berlin", "University of Bonn"
    ],
    "Singapore": [
        "National University of Singapore",
        "Nanyang Technological University",
        "Singapore Management University"
    ]
}

programs = ["Computer Science", "AI", "Data Science", "Business", "Engineering", "MBA"]

data = []

for _ in range(600):  # 600 universities (you can change 500–800)
    country = random.choice(list(countries.keys()))
    uni = random.choice(countries[country])

    cgpa = round(random.uniform(5.5, 9.0), 1)
    ielts = round(random.uniform(5.5, 8.0), 1)
    fee = random.randint(1200000, 5000000)
    acceptance = random.randint(5, 95)
    ranking = random.randint(1, 200)
    program = random.choice(programs)

    data.append([
        uni,
        country,
        program,
        cgpa,
        ielts,
        fee,
        acceptance,
        ranking,
        random.choice(["Low", "Medium", "High"])
    ])

df = pd.DataFrame(data, columns=[
    "University",
    "Country",
    "Program",
    "Min_CGPA",
    "Min_IELTS",
    "Tuition_Fee",
    "Acceptance_Rate",
    "World_Ranking",
    "Job_Prospect"
])

df.to_csv("universities.csv", index=False)

print("✅ 600 universities generated successfully!")
