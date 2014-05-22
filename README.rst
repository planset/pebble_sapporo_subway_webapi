==============
pebble-planset
==============

自分用のpebbleアプリです。


構成
====

* pebble-planset

  * pebble アプリ

* pebble-planset-webapi

  * アプリで使うWeb API 


pebble-planset
==============
* 時刻、日付、曜日表示
* 天気の表示
* 近くの駅の電車出発時刻の表示


pebble-planset-webapi
=======================

Feature
--------
* 札幌の東豊線の情報を配信する。

  * 緯度経度から一番近い駅の情報を取得する
  * 駅の情報とは次のこと。

    * Pebbleアプリに使えるちょうどよい長さの駅名
    * 次の電車発車時刻（福住方面行き、栄町方面行き）


setup
=======
nginx+supervisor+uwsgi

supervisor::

    sudo ln -s /var/vhosts/dkpyn.com/pebble-planset-webapi/supervisor_conf/pebble-planset-webapi.conf  /etc/supervisor/conf.d/


nginx::

    upstream pebble_planset_webapi {
        ip_hash;
        server 127.0.0.1:9091;
    }

    # ======================================================
    # /   pebble-planset-webapi web settings
    # ======================================================
    location ~ ^/pebble/(.*)$ {
        uwsgi_pass pebble_planset_webapi;
        include uwsgi_params;
        uwsgi_param SCRIPT_NAME /pebble;
        uwsgi_param PATH_INFO /$1;
    }



