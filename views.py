from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def haha(request):
    return HttpResponse('haha')

def heihei(request):
    return HttpResponse('heihei')


def xixi(request):
    return HttpResponse('xixi')
