# ディレクトリ構造

.<br>
├── README.md<br>
├── __pycache__<br>
│   └── form.cpython-37.pyc<br>
├── form.py<br>
├── posinega.trim<br>
└── templates<br>
    ├── form.html<br>
    ├── layout.html<br>
    └── result.html<br>

# 必要なライブラリ・ファイル

## 形態素解析器 [Janome](https://mocobeta.github.io/janome/)

```
pip install janome
```

## Twitter API
```
pip install python-twitter
```

## 日本語評価極性辞書（名詞編）ver.1.0（2008年12月版）

[『乾・鈴木研究室』](http://www.cl.ecei.tohoku.ac.jp/index.php?Open%20Resources%2FJapanese%20Sentiment%20Polarity%20Dictionary)から日本語評価極性辞書（名詞編）ver.1.0（2008年12月版）を「posinega.trim」という名前で保存してください。

東山昌彦, 乾健太郎, 松本裕治, 述語の選択選好性に着目した名詞評価極性の獲得, 言語処理学会第14回年次大会論文集, pp.584-587, 2008. / Masahiko Higashiyama, Kentaro Inui, Yuji Matsumoto. Learning Sentiment of Nouns from Selectional Preferences of Verbs and Adjectives, Proceedings of the 14th Annual Meeting of the Association for Natural Language Processing, pp.584-587, 2008.

## dotenv
参考 → [【GitHub】に載せたくない環境変数の書き方 Python](https://qiita.com/hedgehoCrow/items/2fd56ebea463e7fc0f5b)
```
pip install python-dotenv
```

## Twitter APIキー
ファイル名「.env」を作成し、

```
CONSUMER_KEY = "API key"
CONSUMER_SECRET = "API key secret"
ACCESS_TOKEN = "Access token"
ACCESS_TOKEN_SECRET = "Access token secret"
```
を入力してください。

# サーバー起動方法
```
FLASK_APP=form.py FLASK_ENV=developme flask run
```
