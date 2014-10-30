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


setup
=======
herokuにごー::

    git clone [this repository]
    cd [this repository]
    heroku create
    git push heroku master
    heroku ps:scale web=1
    heroku open


