from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todo_db"]
collection = db["todo_items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item = {
        "itemName": request.form.get("itemName"),
        "itemDescription": request.form.get("itemDescription")
    }

    collection.insert_one(item)

    return jsonify({
        "message": "To-Do item saved successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)