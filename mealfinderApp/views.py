# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from models import Restaurant
from serializers import RestaurantSerializer

@csrf_exempt
def findMeal(request):
    if request.method == "POST":
        restaurant = Restaurant.objects.get(name=request.POST['restaurant'])
        return HttpResponse(restaurant.name)
    else:
        return HttpResponse("Invalid request")