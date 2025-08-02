from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path


def home(request):
    return HttpResponse('Ola')
# Create your views here.
