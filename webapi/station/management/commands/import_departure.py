# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand, AppCommand
import requests

from lxml import etree
from station.models import Station, StationDeparture


class Command(BaseCommand):
    args = '<station.json path>'
    help = ''

    def handle(self, *args, **options):
        if len(args) != 1:
            raise Exception('A argument, dia.json path, is required. ex) ../dia.json')
        dia_json_path = args[0]
        with open(dia_json_path) as f:
            diadict = json.load(f, encoding='utf-8')

        hours = list(range(6, 24)) + [0]

        for k,dia in diadict.items():
            station_id = int(k)
            s = Station.objects.get(pk=station_id)
            s.departures.all().delete()
            if s is None:
                continue

            for j in range(2):
                # 栄町と福住（片方しか路線がない駅）
                if dia[j] is None:
                    continue
                holiday = False if j==0 else True
                for hourtimedict in dia[j]:
                    for i in range(2):
                        direction = 'fukuzumi' if i==0 else 'sakaemachi'
                        for hour in hours:
                            hour_key = unicode(str(hour))
                            for time in hourtimedict[hour_key]:
                                sd = StationDeparture()
                                sd.time = "{hour:02d}{time:02d}".format(
                                        hour=hour,time=time)
                                sd.holiday = holiday
                                sd.direction = direction
                                s.departures.add(sd)
                            s.save()
                        

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop
