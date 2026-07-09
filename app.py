from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    with open ('data.json','r') as file:
        data = json.load(file)
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True) 