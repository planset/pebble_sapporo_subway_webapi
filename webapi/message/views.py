#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core import serializers
from django.shortcuts import render_to_response, redirect
#from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound
from django.template import RequestContext

import urllib2
import json
from models import Message

from kata2hira import text2hira

def list_message(request):
    try:
        messages = Message.objects.all().order_by('-id')[:5]
    except Menu.DoesNotExist:
        return HttpResponseNotFound(mimetype='application/json')
    for message in messages:
        message.message = text2hira(message.message).encode('utf-8')
    jsondata = serializers.serialize('plainjson', messages, ensure_ascii=False)
    return HttpResponse(jsondata, mimetype='application/json')


def add_message(request):
    messages = []
    if request.method == 'GET':
        pass
    else:
        message = request.POST.get('message')
        m = Message()
        m.message = message
        m.save()
        messages.append('Successfully!')
    return render_to_response("pebblemessenger/message.html",
            {'messages':messages},
            context_instance=RequestContext(request))


