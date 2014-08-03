# -*- coding: utf-8 -*- 
from django.http import Http404
from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers


def ms_to_filename(ms):
    """for pbi file name"""
    t_ms = ms % 1000
    s = ms // 1000
    t_s = s % 60
    m = s // 60
    t_m = m // 60
    t_h = m // 60
    return "{:02d}_{:02d}_{:02d}_{:03d}".format(t_h, t_m, t_s, t_ms)

def index(request):
    return HttpResponse('index')

def _read_pbi(path):
    try:
        with open(path, 'rb')as f:
            return f.read()
    except:
        raise Http404

def _read_ms(path, default):
    ms = default
    try:
        with open(path) as f:
            ms = int(f.read())
    except:
        pass
    return ms

def _next_ms(path, ms, skip_ms=250):
    ms += skip_ms
    with open(path, 'w') as f:
        f.write(str(ms))

def show(request, id):
    status_file = 'data_pbi/' + str(id) + '/current.txt'
    ms = _read_ms(status_file, 0)
    filename = ms_to_filename(ms) + '.pbi'
    try:
        data = _read_pbi('data_pbi/'+ str(id) + '/' + filename)
    except:
        _next_ms(status_file, 0, 0) # 最後まで行った場合、0msに戻す
        raise
    _next_ms(status_file, ms)
    return HttpResponse(data,
        content_type='application/octet-stream')

def start(request, id):
    return HttpResponse('start' + str(id))

def stop(request, id):
    return HttpResponse('stop' + str(id))
