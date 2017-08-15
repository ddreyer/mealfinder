# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from models import Restaurant
from serializers import RestaurantSerializer

def findMeal(request):
    """ Finds meal based on POST request from client.

    Arguments:
    request -- should contain restaurant name and 
            macros in a matrix (protein, fat, carbs)
    """
    if request.method == "GET":
        restaurant = Restaurant.objects.get(name=request.GET['restaurant'])
        clientMacros = JSON.serialize(request.GET['macros'])
        # find closest meal to fit macros
        for meal in restaurant.meals:

            data = 
        return HttpResponse(restaurant.name)
        # return Response()
    else:
        return HttpResponse("Invalid request")