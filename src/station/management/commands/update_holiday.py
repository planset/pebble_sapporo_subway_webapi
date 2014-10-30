# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import requests

from lxml import etree
from station.models import Holiday


urlbase = 'http://www.google.com/calendar/feeds/outid3el0qkcrsuf89fltf7a4qbacgt9@import.calendar.google.com/public/full-noattendees?start-min={}&start-max={}'

namespaces = {
    'ns': 'http://www.w3.org/2005/Atom',
    'gd': 'http://schemas.google.com/g/2005'
}

class Command(BaseCommand):
    args = '<start_date> <end_date>'
    help = ''

    def handle(self, *args, **options):
        if len(args) == 0:
            import datetime
            year = datetime.datetime.now().year
            args = ('{}-01-01'.format(year), '{}-12-31'.format(year))
        if len(args) != 2:
            raise Exception('Arguments, startdate and enddate, are required. ex) 2014-01-01 2014-12-31')
        startdate = args[0]
        enddate = args[1]
        url = urlbase.format(startdate, enddate)
        res = requests.get(url)
        root = etree.fromstring(res.content)
        entries = root.xpath('//ns:entry', namespaces=namespaces)
        for entry in entries:
            entry_start_time = entry.xpath('.//gd:when/@startTime', namespaces=namespaces)[0]
            entry_title = entry.xpath('.//ns:title/text()', namespaces=namespaces)[0]
            holiday = Holiday.objects.filter(date=entry_start_time).first() or Holiday.objects.create()
            holiday.date = entry_start_time
            holiday.name = entry_title
            holiday.save()

