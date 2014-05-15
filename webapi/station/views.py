# -*- coding: utf-8 -*- 
from math import acos, sin, cos, radians
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers

from helpers import jsonalize
import json
import models

class Location(object):
    def __init__(self, lat, lng):
        self.lat = float(lat)
        self.lng = float(lng)

def show(request, id):
    data = get_object_or_404(models.Station, id=1)
    data = jsonalize(data)
    return HttpResponse(data, content_type='application/json;charset=utf-8')


def is_holiday(date):
    h = models.Holiday.objects.filter(date=date).first()
    return h is not None


def _closest_station(stations, current_loc):
    result = None
    m = 9999999
    for station in stations:
        lat1rad = radians(current_loc.lat)
        lat2rad = radians(station.lat)
        dis = acos(sin(lat1rad) * sin(lat2rad) + cos(lat1rad) * cos(lat2rad) * cos(radians(station.lng) - radians(current_loc.lng))) * 6378.1
        if m > dis:
            m = dis
            result = station
    return result 

def add_colon(db_time):
    return db_time[:2] + ':' + db_time[2:]

def closest(request, lat, lng):
    stations = models.Station.objects.all()
    station = _closest_station(stations, Location(lat, lng))
    now = datetime.now()
    time_string = now.strftime('%H%m')
    next_fukuzumi_departure = None
    next_sakaemachi_departure = None
    f = is_holiday(now.strftime('%Y-%M-%d'))
    for departure in station.departures_by_direction('fukuzumi', f).all():
        if departure.time > time_string:
            next_fukuzumi_departure = departure
            break
    for departure in station.departures_by_direction('sakaemachi', f).all():
        if departure.time > time_string:
            next_sakaemachi_departure = departure
            break
    dir1time = add_colon(next_sakaemachi_departure.time) if next_sakaemachi_departure else ''
    dir2time = add_colon(next_fukuzumi_departure.time) if next_fukuzumi_departure else ''
    data = {
            'stationInfoName': station.name,
            'stationInfoDir1': u'栄町',
            'stationInfoDir2': u'福住',
            'stationInfoDir1Departure': dir1time,
            'stationInfoDir2Departure': dir2time
            }
    #data = jsonalize(data)
    #data = serializers.serialize('plainjson', data, ensure_ascii=False)
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data, mimetype='application/json;charset=utf-8')

def departures(request, station_id):
    data = get_object_or_404(models.Station, id=1)
    data = jsonalize(data.departures)
    return HttpResponse(data, mimetype='application/json;charset=utf-8')
