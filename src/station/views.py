# -*- coding: utf-8 -*- 
from math import acos, sin, cos, radians
from datetime import datetime

import pytz
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .helpers import jsonalize
import json
from . import models

class Location(object):
    def __init__(self, lat, lng):
        self.lat = float(lat)
        self.lng = float(lng)

def show(request, id):
    data = get_object_or_404(models.Station, id=1)
    data = jsonalize(data)
    return HttpResponse(data, content_type='application/json;charset=utf-8')


def is_holiday(date):
    """
    :param date datetime.date: 指定した日付
    :return True/False: True:土日祝日, False:平日
    """
    if date.weekday() in (5, 6):
        return True
    h = models.Holiday.objects.filter(date=date.strftime('%Y-%m-%d')).first()
    return h is not None


def _closest_station(stations, current_loc):
    result = None
    m = 9999999
    for station in stations:
        lat1rad = radians(current_loc.lat)
        lat2rad = radians(station.lat)
        dis = acos(sin(lat1rad) * sin(lat2rad) + cos(lat1rad) * cos(lat2rad) * cos(radians(station.lng) - radians(current_loc.lng))) * 6378.1
        if dis < m:
            m = dis
            result = station
    return result 

def add_colon(db_time):
    return db_time[:2] + ':' + db_time[2:]

def closest(request, lat, lng):
    stations = models.Station.objects.all()
    station = _closest_station(stations, Location(lat, lng))
    jst = pytz.timezone('Asia/Tokyo')
    now = datetime.now(jst)
    time_string = now.strftime('%H%M')
    next_fukuzumi_departure = None
    next_sakaemachi_departure = None
    f = is_holiday(now)
    for departure in station.departures_by_direction('sakaemachi', f).all():
        if departure.time > time_string:
            next_sakaemachi_departure = departure
            break
    for departure in station.departures_by_direction('fukuzumi', f).all():
        if departure.time > time_string:
            next_fukuzumi_departure = departure
            break
    dir1time = add_colon(next_sakaemachi_departure.time) if next_sakaemachi_departure else ''
    dir2time = add_colon(next_fukuzumi_departure.time) if next_fukuzumi_departure else ''
    data = {
            u'stationInfoName': unicode(station.name_for_pebble),
            u'stationInfoDir1': u'さかえ町',
            u'stationInfoDir2': u'福住',
            u'stationInfoDir1Departure': unicode(dir1time),
            u'stationInfoDir2Departure': unicode(dir2time),
            u'datetime': str(now)
            }
    data = json.dumps(data, ensure_ascii=False, encoding='utf-8')
    return HttpResponse(data, content_type='application/json;charset=utf-8')

def departures(request, station_id):
    data = get_object_or_404(models.Station, id=1)
    data = jsonalize(data.departures)
    return HttpResponse(data, content_type='application/json;charset=utf-8')
