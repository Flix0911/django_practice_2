from django.shortcuts import render
# we're not rending, we're taking in jsonresponse to send json responess
from django.http import JsonResponse

# Weird thing about django/python. Back in JS, it was easy to take an object and convert to json. JSON is JS
# Python is not as easy. You must use a serializer 
# Serializer for turning python objects into JSON
# This case, convert to JSON strings
from django.core.serializers import serialize

# need JSON module
# import json module to convert in and out of json
# this is built into pyton, it's a python module, while everything else is from django
import json

# we need our turtle model
from pets.models import Turtle

# Django View Class for class based views
# allows us to create a class with function from that method is occuring
from django.views import View

# Our help function for getting the request body
from pets.helpers import GetBody


# Create your views here.

# class for "/turtle", 
class TurtleView(View):
    # INDEX route (get to /turtle)
    def get(self, request):
        # get all the rurtles
        all = Turtle.objects.all()
        # don't need a list from the all, because it already sends a list/array
        # Turn all the objects into a json string
        serialized = serialize("json", all)
        # json string will now be turned into objects (dictonary in python)
        finalData = json.loads(serialized)
        # send the json response, using the dictionary
        # We need to also turn off some security features, safe=False
        return JsonResponse(finalData, safe=False)

    # Create route (post to /turtle)
    def post(self, request):
        # get the request body
        body = GetBody(request)
        # Create a new turtle
        turtle = Turtle.objects.create(
            # what we receive is a python object. We need to turn to json object
            name = body["name"],
            age = body["age"]
        )
        # Turn the python object into json and back into a dictionary, just like above
        # json wants a list[] or tuple
        finalData = json.loads(serialize("json", [turtle]))
        # Send the response
        # Again, safe=False
        return JsonResponse(finalData, safe=False)
    
# class for "/turtle/<id>"
class TurtleViewID(View):
    # Show route (GET to /turtle/:id)
    def get(self, request, id):
        # get the turtle requested
        turtle = Turtle.objects.get(id=id)
        # serialize into dictionary
        finalData = json.loads(serialize("json", [turtle]))
        return JsonResponse(finalData, safe=False)
    
    # Update route (PUT to /turtle/:id)
    def put(self, request, id):
        # Get the body of the id
        body = GetBody(request)
        # Update the Turtle ~ spot operator (** works like the spread operator in JS)
        # grab the Turtle with the right ID and then update it (the body)
        Turtle.objects.filter(id=id).update(**body)
        # Query the updated Turtle
        turtle = Turtle.objects.get(id=id)
        # Serialize it because it must be a dictionary
        finalData = json.loads(serialize("json", [turtle]))
        # Send the response
        return JsonResponse(finalData, safe=False)
    
    # Delete route (delete to /turtle/:id)
    def delete(self, request, id):
        # Query the turtle we want to delete
        turtle = Turtle.objects.get(id=id)
        # Delete the turtle
        turtle.delete()
        # serialize
        finalData = json.loads(serialize("json", [turtle]))
        # send the response
        return JsonResponse(finalData, safe=False)