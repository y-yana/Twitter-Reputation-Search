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

    names = []

    names.append(request.form["name1"])
    names.append(request.form["name2"])
    names.append(request.form["name3"])
    names.append(request.form["name4"])
    names.append(request.form["name5"])
    pers = []

    for name in names:
        if(name == ""):
            pers.append(0)
        else:
            query = urlencode({
                'q': request.form[name],  # 検索ワード
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
            p_per = 0

            tokenizer = Tokenizer()

            for sentence in sentenses:
                for token in tokenizer.tokenize(sentence):
                    t = token.base_form  # 基本形に直す
                    if data.get(t) != None:  # 辞書にあったら
                        if data.get(t) == 1:  # ポジティブと判定されたら
                            ptotal += 1
                        else:
                            ntotal += 1

            if not ptotal+ntotal == 0:
                p_per = int(ptotal/(ptotal+ntotal)*100)

            pers.append(p_per)

    return name[0], name[1], name[2], name[3], name[4], pers[0], pers[1], pers[2], pers[3], pers[4]
