# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Restaurant

def findMeal(request):
    if request.method == "GET":
        restaurant = Restaurant.get(name=request.GET['restaurant'])
        return HttpResponse(restaurant)
    else:
        return HttpResponse("Invalid request")