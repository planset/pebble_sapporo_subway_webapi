# -*- coding: utf-8 -*-
import json

from django.core.management.base import BaseCommand

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

        for station_id_str,dia in diadict.items():
            station_id = int(station_id_str)
            s = Station.objects.get(pk=station_id)
            if s is None:
                continue
            s.departures.all().delete()

            #0:平日、1;休日
            for holiday_id in range(2):
                # 栄町と福住（片方しか路線がない駅）
                if dia[holiday_id] is None:
                    continue

                is_holiday = False if holiday_id==0 else True

                #dia[holiday_id][0]が福住行き、dia[holiday_id][1]が栄町行き
                for direction_id in range(2):
                    direction = 'fukuzumi' if direction_id==0 else 'sakaemachi'
                    for hour, minutes in dia[holiday_id][direction_id].items():
                        for minute in minutes:
                            hour = int(hour)
                            minute = int(minute)
                            sd = StationDeparture()
                            sd.time = "{hour:02d}{minute:02d}".format(
                                    hour=hour,minute=minute)
                            sd.holiday = is_holiday
                            sd.direction = direction
                            s.departures.add(sd)
                        s.save()
                        

# vim: tabstop=4 shiftwidth=4 expandtab softtabstop
