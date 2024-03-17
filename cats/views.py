from django.shortcuts import render
# take in jsonresponse
from django.http import JsonResponse
# serialize the json strings
from django.core.serializers import serialize
# need JSON from python
import json
# need the Cat model
from cats.models import Cat
# Need View class
from django.views import View
# need to be able to grab the request body
from cats.helpers import GetBody

# Create your views here.

# Class for "/cat/"
class Cat_View(View):
    # Index route (GET to /cat/)
    def get(self, request):
        # GET all cats
        all = Cat.objects.all()
        # GET object into json string ~ serialize
        serialized = serialize("json", all)
        # Variable for the serialization
        Final_Data = json.loads(serialized)
        # return
        return JsonResponse(Final_Data, safe=False)
    
    # CREATE route(POST to /cat/)
    def post(self, request):
        # grab the request body
        body = GetBody(request)
        # Create the new Cat
        cat = Cat.objects.create(
            name = body["name"],
            breed = body["breed"],
            age = body["age"],
            sex = body["sex"],
            price = body["price"]
        )
        # Grab again and serialize
        Final_Data = json.loads(serialize("json", [cat]))
        # POST the cat to be returned
        return JsonResponse(Final_Data, safe=False)
    
# Class for "/cat/<id>"
class Cat_View_ID(View):
    # SHOW route(GET to /cat/<id>/)
    def get(self, request, id):
        # GET cat by id
        cat = Cat.objects.get(id=id)
        # serialize
        Final_Data = json.loads(serialize("json", [cat]))
        # return
        return JsonResponse(Final_Data, safe=False)
    # UPDATE route(PUT to /cat/<id>/)
    def put(self, request, id):
        # grab the body of the ID
        body = GetBody(request)
        # grab with spot operator and update the body
        Cat.objects.filter(id=id).update(**body)
        # query the cat to be updated
        cat = Cat.objects.get(id=id)
        # seralize
        Final_Data = json.loads(serialize("json", [cat]))
        # return the response
        return JsonResponse(Final_Data, safe=False)
        
    # DELETE route(DELETE to /cat/<id>/)
    def delete(self, request, id):
        # query the cat by ID to be deleted
        cat = Cat.objects.get(id=id)
        # delete it
        cat.delete()
        # serialize
        Final_Data = json.loads(serialize("json", [cat]))
        # send the response
        return JsonResponse(Final_Data, safe=False)