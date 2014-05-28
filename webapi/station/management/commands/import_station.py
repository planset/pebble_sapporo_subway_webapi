# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand, AppCommand
import requests

from lxml import etree
from station.models import Station


class Command(BaseCommand):
    args = '<station.json path>'
    help = ''

    def handle(self, *args, **options):
        if len(args) != 1:
            raise Exception('A argument, station.json path, is required. ex) ../station.json')
        station_json_path = args[0]
        with open(station_json_path) as f:
            stations = json.load(f, encoding='utf-8')

        for station in stations:
            id = int(station[0])
            s = Station.objects.filter(id=id).first() or Station.objects.create()
            s.id = id
            s.name = station[2]
            s.name_for_pebble = station[3]
            s.description = station[1]
            s.lat = float(station[4])
            s.lng = float(station[5])
            s.save()
            

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop
