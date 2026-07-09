from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://kirtisonje2908_db_user:Kirti0909@cluster0.lorq5km.mongodb.net/?appName=Cluster0")

db = client["student_db"]
collection = db["students"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():

    try:
        name = request.form["name"]
        email = request.form["email"]

        data = {
            "name": name,
            "email": email
        }

        collection.insert_one(data)

        return render_template("success.html")

    except Exception as e:
        return render_template("index.html", error=str(e))


if __name__ == "__main__":
    app.run(debug=True)