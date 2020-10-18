import twitter
from janome.tokenizer import Tokenizer
from urllib.parse import urlencode
from flask import Flask, request, render_template
import os
from os.path import join, dirname
from dotenv import load_dotenv
import twitter_search as ts
import twitter_search2 as ts2

app = Flask(__name__)


@app.route("/")
def show():
    return render_template("form.html")


@app.route("/2")
def show2():
    return render_template("form2.html")


@app.route("/result", methods=["POST"])
def result():
    message, name, p_per, n_per, m_per, p_sen1, p_sen2, p_sen3, n_sen1, n_sen2, n_sen3 = ts.search()
    return render_template("result.html", message=message, name=name, p_per=p_per, n_per=n_per, m_per=m_per, p_sen1=p_sen1, p_sen2=p_sen2, p_sen3=p_sen3, n_sen1=n_sen1, n_sen2=n_sen2, n_sen3=n_sen3)


@app.route("/result2", methods=["POST"])
def result2():
    name1, name2, name3, name4, name5, per1, per2, per3, per4, per5 = ts2.search()
    return render_template("result2.html", name1=name1, name2=name2, name3=name3, name4=name4, name5=name5, per1=per1, per2=per2, per3=per3, per4=per4, per5=per5)

    # おまじない
if __name__ == "__main__":
    app.run(debug=True)
