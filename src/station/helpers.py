# -*- coding: utf-8 -*-
import json
from django.db import models as django_models
from django.db.models.query import QuerySet

def jsonalize(item):
    return json.dumps(item, ensure_ascii=False, default=model_to_json)

def model_to_json(obj):
    if isinstance(obj, django_models.Model):
        return obj.to_json()
    elif isinstance(obj, QuerySet):
        return list(obj)
    else:
        raise TypeError(repr(obj) + " is not JSON serializable")

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
