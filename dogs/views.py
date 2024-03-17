from django.shortcuts import render #useless in this case
# taking in a jsonresponse to send json respones
from django.http import JsonResponse
# need to serialize the json strings
from django.core.serializers import serialize
# need JSON
import json
# need the dog model
from dogs.models import Dog
# need the view class so we can use functions fomr the method that is occuring
from django.views import View
# need to grab the body of the request
from dogs.helpers import GetBody

# Create your views here.


# Class for "/dog/"
class Dog_View(View):
    # INDEX route (GET to /dog/)
    def get(self, request):
        # GET all the dogs
        all = Dog.objects.all()
        # Get all objects into a JSON string ~ Serialize
        serialized = serialize("json", all)
        # Variable for serialized JSON
        Final_Data = json.loads(serialized)
        # return the GET request
        return JsonResponse(Final_Data, safe=False)
    
    # CREATE route (POST to /dog/)
    def post(self, request):
        # Grab the request body
        body = GetBody(request)
        # Create the new Dog
        dog = Dog.objects.create(
            # What is received is a python object, we need JSON
            name = body["name"],
            breed = body["breed"],
            age = body["age"],
            color = body["color"]
        )
        # Grab created and serialize
        Final_Data = json.loads(serialize("json", [dog]))
        # POST dog to the return
        return JsonResponse(Final_Data, safe=False)
    
# Class for "/dog/<id>"
class Dog_View_ID(View):
    # SHOW route(GET to /dog/<id>/)
    def get(self, request, id):
        # GET dog by ID
        dog = Dog.objects.get(id=id)        
        # Variable for serialized dog
        Final_Data = json.loads(serialize("json", [dog]))
        # Return the GET request
        return JsonResponse(Final_Data, safe=False)
    
    # Update route(PUT to /dog/<id>/)
    def put(self, request, id):
        # GET body of the ID
        body = GetBody(request)
        # Grab dog with spot operator and update the body
        Dog.objects.filter(id=id).update(**body)
        # query the updated dog
        dog = Dog.objects.get(id=id)
        # serialize because it must be a dict
        Final_Data = json.loads(serialize("json", [dog]))
        # send the response
        return JsonResponse(Final_Data, safe=False)
    
    # Delete route(DELETE to /dog/<id>)
    def delete(self, request, id):
        # query the dog by ID that is to be deleted
        dog = Dog.objects.get(id=id)
        # Delete it
        dog.delete()
        # serialize 
        Final_Data = json.loads(serialize("json", [dog]))
        # send the response
        return JsonResponse(Final_Data, safe=False)