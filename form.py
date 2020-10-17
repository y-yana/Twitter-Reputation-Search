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
        'lang': 'ja',
        'count': 100  # 取得するツイート数（最大100個まで）
    })

    # ツイートを取得してsentencesに追加
    sentenses = []
    result = api.GetSearch(raw_query=query)
    for status in result:
        sentenses.append(status.text)

    ptotal = 0
    ntotal = 0
    positive_words = []
    negative_words = []

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
                    if len(positive_words) < 10 and not(t in positive_words):
                        positive_words.append(t)
                else:
                    # print("ネガティブ"+t)
                    n += 1
                    if len(negative_words) < 10 and not(t in negative_words):
                        negative_words.append(t)

        ptotal += p
        ntotal += n
    p_sentence = ', '.join(positive_words)
    n_sentence = ', '.join(negative_words)

    name = request.form["name"]
    p_per = int(ptotal/(ptotal+ntotal)*100)
    n_per = 100 - p_per
    message = ""
    if p_per > 80:
        message = "Very Good"
    elif p_per > 65:
        message = "Good"
    elif p_per > 40:
        message = "Normal"
    else:
        message = "Bad"

    return render_template("result.html", message=message, name=name, p_per=p_per, n_per=n_per, p_sentence=p_sentence, n_sentence=n_sentence)


# おまじない
if __name__ == "__main__":
    app.run(debug=True)
