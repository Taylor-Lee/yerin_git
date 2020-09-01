from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import random

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/showCat', methods=['GET'])
def read_articles():
    cats = list(db.cats.find({}, {'_id': False}))
    cat = random.choice(cats)
    return jsonify({'result': 'success', 'cat': cat})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

    # app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > figure > div > div._3A74U > div > div > a > div > img