==============
pebble-planset
==============

札幌の地下鉄（東豊線）の最寄りの駅の次の電車の時刻を表示するpebbleappのウェブサーバー側です。


pebble-planset-webapi
=======================

Feature
--------
* 札幌の東豊線の情報を配信する。

  * 緯度経度から一番近い駅の情報を取得する
  * 駅の情報

    * Pebbleアプリに使えるちょうどよい長さの駅名
    * 次の電車発車時刻（福住方面行き、栄町方面行き）


development
===========
terminal::

    git clone [this repository]
    cd [this repository]
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    #foreman start
    python src/manage.py runserver


http://localhost:8000/stations/closest/0/0/ にアクセスして情報が取得できていればよい。


deployment
===========
heroku::

    git clone [this repository]
    cd [this repository]
    heroku create
    git push heroku master
    heroku ps:scale web=1
    heroku config:set APP_ENV=production
    heroku config:set SECRET_KEY="{REPLACE YOUR SECRET_KEY}"
    heroku open


