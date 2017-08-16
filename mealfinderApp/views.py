# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from nutritionix import Nutritionix

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

        if restaurant is None:  # if not found, query Nutritionix database
            nix = Nutritionix()
            nix.search("%s" % restaurant ).nxql(
                filters={
                    "item_type":1
                },
                fields=["item_name", "item_id", "nf_calories"]
            ).json()
            
        clientMacros = JSON.serialize(request.GET['macros'])

        # find closest meal to fit macros
        for meal in restaurant.meals:
            # query application database

            
            data = 
        return HttpResponse(restaurant.name)
        # return Response()
    else:
        return HttpResponse("Invalid request")