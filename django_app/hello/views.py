from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    params = {
        'title': 'Hello/Index',
        'msg': 'これは，サンプルでつくったページです',
        'goto': 'next'
    }
    return render(request, 'hello/index.html', params)


def next(request):
    params = {
        'title': 'Hello/Next',
        'msg': 'これは，もうひとつのページです',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)
