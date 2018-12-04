# olive-api
This is the Api server for olive project  
**build by django REST framework**

<img src="http://zett.work/d_is_silent.gif" alt="" />
<br /><br />

## Requirement(Local)
- Docker for mac (メモリの割り当てを4GBくらいに増やしても良い)

<br />

## Dependencies
- Python 3.6.6
- Postgres 10.5

- Django
    - django==2.0
    - psypopg2-binary
    - djangorestframework
    - markdown
    - django-filter
    - pygraphviz
    - django-extensions

<br />

## Setup 
#### 1/4 - Clone and migrate
```terminal
git clone https://github.com/creative-mintzplanning/nu-api.git

cd olive-api/

make start
```
無事dockerが起動したらdjangoのサーバーが立ち上がってるはずです。  
今は一旦 **ctrl + C**で抜けて次の手順に進みます。


<br />

#### 2/4 - Initialize data for DB
```terminal
make pre-migrate

make update
```
localのsuperuserは好きに設定してください。  
seedにデータを追加したいときは => ./fixtures/seed.json に追加してください。

<br />

#### 3/4 - Start
```terminal
make start
```
このコマンドで最終的にdocker containerを起動させます。  
もしここでコケても、ctrl+cしてもう一度make startしてみてください。
<br>

#### 4/4 - Test

<a href src="http://localhost:8008/">http://localhost:8008/</a>

まずはトップページに繋がるか確認しましょう。
```terminal
curl http://localhost:8008/api/
```
実際にデータが取得できればひとまずOKだと思います。  

shell内でデータベースに接続したい時は以下のコマンドで接続できます。  
password: postgres
```
make connectdb
```
お疲れ様でした！

**※何かコマンドを実行するときの注意  
django内では通常、「python manage.py」 に続けてコマンドを入力しますが、  
djangoはあくまでdocker-composeの中の、  
「api」というcontainerの中で実行されているので、  
毎回「docker-compose run api」を頭に付けてコマンド実行してください。**

<br>

## Makefile Commands
新たにmigrateしたい時　↓
```
make migrate
```

seedデータを読み込みたい時　↓
```
make seed
```

開発環境を起動する時　↓
```
make start
```

<br>

## Superuser inside django


<br>

## Entity Relationship Diagram

<br>

## API document
<a href="http://localhost:8008/api-docs/">http://localhost:8008/api-docs/</a>

<br>

## API console
<a href="http://localhost:8008/api/">http://localhost:8008/api/</a>

<br> 

## Tasks


<br>

## Reviews
みんなでレビューしましょう。  
わからなくてもコードを読みましょう。  
質問しましょう、指摘しましょう。改善していきましょう。  
みんなで作りましょう。

<br>

## Prefixes
- hot: 緊急かつ重大な修正
- feat：新しい機能追加
- fix：バグフィックス
- wip: 進行中がだ、コードをメンバーに公開


- docs：ドキュメントのみ変更
- style：コードの挙動に影響を与えない変更（空白、フォーマット、セミコロンの欠落など）
- refactor：バグを修正したり、機能を追加したりしないコード変更
- perf：パフォーマンスを向上させるコード変更
- test：既存のテストの欠落または修正の追加
