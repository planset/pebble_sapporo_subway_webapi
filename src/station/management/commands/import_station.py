# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand

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
            id = int(station['station_id'])
            s = Station.objects.filter(id=id).first() or Station.objects.create()
            s.id = id
            s.name = station['station_name']
            s.name_for_pebble = station['station_name_for_pebble']
            s.description = station['pdf_file_name']
            s.lat = float(station['fX'])
            s.lng = float(station['fY'])
            s.save()
            
