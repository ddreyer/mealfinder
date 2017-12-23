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
        restaurant_name = request.GET['restaurant']

        # for testing purposes
        #Restaurant.objects.get(name=restaurant_name).delete()

        try:
            # Query restaurant items
            restaurant = Restaurant.objects.get(name=restaurant_name)

        except Exception as e:  # if not found, query Nutritionix database

            # query database
            nix = Nutritionix()
            nixResults = nix.search().nxql(
                queries={
                    "brand_name":"%s" % restaurant_name
                },
                filters={
                    "item_type":1
                },
                fields=["item_name", "nf_total_fat", 
                    "nf_total_carbohydrate", "nf_protein"]
            ).json()

            # Invalid restaurant name returns no results
            if (nixResults["total"] == 0):
                return HttpResponse("Invalid request")

            # Store restaurant items into DB
            items = []
            for item in nixResults["hits"]:
                items.append(item["fields"])

            Restaurant.objects.create(
                name=restaurant_name,
                items=items
            )

            # Query restaurant items
            restaurant = Restaurant.objects.get(name=restaurant_name)

        clientMacros = request.GET['macros']
        items = restaurant.items
        # find closest meal to fit macros
        # for meal in restaurant.items:
        #     item = meal

        return HttpResponse(restaurant.items)
    else:
        return HttpResponse("Invalid request")