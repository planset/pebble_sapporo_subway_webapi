# -*- coding: utf-8 -*- 
from django.http import Http404
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers

def index(request):
    return HttpResponse('index')

def _read_pbi(path, default):
    try:
        with open('data_pbi/sample.pbi', 'rb')as f:
            return f.read()
    except:
        raise Http404

def show(request, id):
    data = _read_pbi('data_pbi/sample.pbi', None)
    return HttpResponse(data,
        content_type='application/octet-stream')

def start(request, id):
    return HttpResponse('start' + str(id))

def stop(request, id):
    return HttpResponse('stop' + str(id))
