from django.db import models
from helpers import jsonalize


class Holiday(models.Model):
    date = models.CharField(max_length=10)
    name = models.CharField(max_length=255, default='')


class Station(models.Model):
    name = models.CharField(max_length=255, default='')
    name_for_pebble = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def departures_by_direction(self, direction, is_holiday):
        return self.departures.filter(direction=direction, holiday=is_holiday).order_by('time')

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'name_for_pebble': self.name_for_pebble,
            'description': self.description,
            'lat': self.lat,
            'lng': self.lng,
            #'departures': [departure.to_json() for departure in self.departures.all()]
            }


class StationDeparture(models.Model):
    time = models.CharField(max_length=4, default='')
    holiday = models.BooleanField(default=False)
    direction = models.CharField(max_length=30, default='fukuzumi') # fukuzumi or sakaemachi
    station = models.ForeignKey(Station, related_name='departures', limit_choices_to={'direction': 'fukuzumi'})

    def to_json(self):
        return {
            'id': self.id,
            'time': self.time,
            'direction': self.direction,
            'holiday': self.holiday
            }


