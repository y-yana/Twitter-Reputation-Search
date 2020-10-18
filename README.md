# Twitter Reputation Search

ワードを入力するとネガポジ判定ができ、Twitter での評判を知ることができます！複数のワードの入力にも対応しているため、比較もできます！きのことたけのこの現在の戦闘力も確認できたり...！？

## アプリの URL

https://shielded-mesa-12200.herokuapp.com

## 使用技術

- フロント

  - HTML
  - CSS
  - Sass
  - JavaScript
  - Chart.js

- サーバーサイド
  - Python
  - Flask
- Twitter API
- Janome (形態素分析)

## アプリの詳細

Twitter API で取得したツイートを Janome で形態素分析をし、日本語極性辞書の値を使ってポジネガ判定をしています。

---

# ディレクトリ構造

```
├── README.md
├── __pycache__
│   └── form.cpython-37.pyc
├── form.py
├── posinega.trim
├── static
│    ├── image
│    ├── js
│    └── style
├── templates
│    ├── form.html
│    ├── form2.html
│    ├── layout.html
│    ├── result.html
│    └── result2.html
├── twitter_search.py
└── twitter_search2.py

```

# 必要なライブラリ・ファイル

## Flask

```
pip install Flask
```

## 形態素解析器 [Janome](https://mocobeta.github.io/janome/)

```
pip install janome
```

## Twitter API

```
pip install python-twitter
```

## 日本語評価極性辞書（名詞編）ver.1.0（2008 年 12 月版）

[『乾・鈴木研究室』](http://www.cl.ecei.tohoku.ac.jp/index.php?Open%20Resources%2FJapanese%20Sentiment%20Polarity%20Dictionary)から日本語評価極性辞書（名詞編）ver.1.0（2008 年 12 月版）を「posinega.trim」という名前で保存してください。

東山昌彦, 乾健太郎, 松本裕治, 述語の選択選好性に着目した名詞評価極性の獲得, 言語処理学会第 14 回年次大会論文集, pp.584-587, 2008. / Masahiko Higashiyama, Kentaro Inui, Yuji Matsumoto. Learning Sentiment of Nouns from Selectional Preferences of Verbs and Adjectives, Proceedings of the 14th Annual Meeting of the Association for Natural Language Processing, pp.584-587, 2008.

## dotenv

参考 → [【GitHub】に載せたくない環境変数の書き方 Python](https://qiita.com/hedgehoCrow/items/2fd56ebea463e7fc0f5b)

```
pip install python-dotenv
```

## Twitter API キー

ファイル名「.env」を作成し、

```
CONSUMER_KEY = "API key"
CONSUMER_SECRET = "API key secret"
ACCESS_TOKEN = "Access token"
ACCESS_TOKEN_SECRET = "Access token secret"
```

を入力してください。

# 実行

```
python form.py
```
