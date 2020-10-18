import twitter
from janome.tokenizer import Tokenizer
from urllib.parse import urlencode
from flask import Flask, request, render_template
import os
from os.path import join, dirname
from dotenv import load_dotenv


def search():

    # 『日本語評価極性辞書』を使用する場合
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

    # 『単語感情極性対応表』を使用する場合
    # path = 'posinega2.txt'
    # with open(path, encoding="utf-8_sig") as f:
    #     lines = f.readlines()

    # # 言葉と数値（ポジティブな言葉は+1、ネガティブな言葉は-1）を格納する
    # data = {}

    # cnt = 0

    # for line in lines:
    #     l = line.split(':')  # タブで分割
    #     if len(l) <= 3:
    #         continue
    #     if cnt < 100:
    #         print(l)
    #         print(l[2])
    #         cnt += 1
    #     if float(l[3]) > 0:
    #         data[l[0]] = 1
    #     elif float(l[3]) < 0:
    #         data[l[0]] = -1
    #     else:
    #         data[l[0]] = 0

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
        for token in tokenizer.tokenize(sentence):
            t = token.base_form  # 基本形に直す
            if data.get(t) != None:  # 辞書にあったら
                if data.get(t) == 1:  # ポジティブと判定されたら
                    ptotal += 1
                    if len(positive_words) < 9 and not(t in positive_words):
                        positive_words.append(t)
                else:
                    ntotal += 1
                    if len(negative_words) < 9 and not(t in negative_words):
                        negative_words.append(t)

    p_sentence1 = ', '.join(positive_words[0:3])
    p_sentence2 = ', '.join(positive_words[3:6])
    p_sentence3 = ', '.join(positive_words[6:])
    n_sentence1 = ', '.join(negative_words[0:3])
    n_sentence2 = ', '.join(negative_words[3:6])
    n_sentence3 = ', '.join(negative_words[6:])

    m_per = 100
    n_per = 0
    p_per = 0

    if not ptotal+ntotal == 0:
        p_per = int(ptotal/(ptotal+ntotal)*100)
        n_per = int(ntotal/(ptotal+ntotal)*100)
        m_per = 0

    # 割合によってメッセージを変更

    message = ""
    if m_per == 100:
        message = "None"
    elif p_per > 80:
        message = "Very Good"
    elif p_per > 65:
        message = "Good"
    elif p_per > 40:
        message = "Normal"
    else:
        message = "Bad"

    name = request.form["name"]

    return message, name, p_per, n_per, m_per, p_sentence1, p_sentence2, p_sentence3, n_sentence1, n_sentence2, n_sentence3
