import twitter
from janome.tokenizer import Tokenizer
from urllib.parse import urlencode
from flask import Flask, request, render_template
import os
from os.path import join, dirname
from dotenv import load_dotenv

app = Flask(__name__)


@app.route("/")
def show():
    message = "Hello World"
    return render_template("form.html", message=message)


@app.route("/result", methods=["POST"])
def result():
    # ファイルを開ける
    path = 'posinega.trim'
    with open(path, encoding="utf-8_sig") as f:
        lines = f.readlines()

    # 言葉と数値（ポジティブな言葉は+1、ネガティブな言葉は-1）を格納する
    data = {}

    for line in lines:
        l = line.split('\t')  # タブで分割
        if l[1] == 'p':
            data[l[0]] = 1
        elif l[1] == 'n':
            data[l[0]] = -1

    CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = os.environ.get(
        "CONSUMER_SECRET")
    ACCESS_TOKEN = os.environ.get(
        "ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = os.environ.get(
        "ACCESS_TOKEN_SECRET")

    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)

    query = urlencode({
        'q': request.form["name"],  # 検索ワード
        'result_type': 'recent',  # 最近のツイートを取得する
        'count': 100  # 取得するツイート数（最大100個まで）
    })

    # ツイートを取得してsentencesに追加
    sentenses = []

    result = api.GetSearch(raw_query=query)
    for status in result:
        sentenses.append(status.text)

    ptotal = 0
    ntotal = 0
    most_positive_sentence = ""
    most_negative_sentence = ""
    most_positive = 0
    most_negative = 0

    tokenizer = Tokenizer()

    for sentence in sentenses:
        p = 0
        n = 0
        # print("---------sentence----------")
        # print(sentence)
        for token in tokenizer.tokenize(sentence):
            t = token.base_form  # 基本形に直す
            if data.get(t) != None:  # 辞書にあったら
                if data.get(t) == 1:  # ポジティブと判定されたら
                    # print("ポジティブ"+t)
                    p += 1
                else:
                    # print("ネガティブ"+t)
                    n += 1
            if p > most_positive:
                most_positive = p
                most_positive_sentence = sentence
            if n > most_negative:
                most_negative = n
                most_negative_sentence = sentence
        ptotal += p
        ntotal += n

    name = request.form["name"]
    return render_template("result.html", name=name, ptotal=ptotal, ntotal=ntotal, most_positive_sentence=most_positive_sentence, most_negative_sentence=most_negative_sentence)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
