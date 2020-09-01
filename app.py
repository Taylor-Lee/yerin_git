from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mypage')
def my_page():
    return 'This is My Page!'

@app.route('/content')
def get_content():
    # 1. DB 에서 content 1개 Random 으로 가져오기
    # 2. client 에 JSON 형태로 내려주기
    # {
    #   content = "오늘 최선이 내 인생의 최선이다."
    # }

    randomContent = {
      "content": "오늘 최선이 내 인생의 최선이다."
    }

    return jsonify(randomContent)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
