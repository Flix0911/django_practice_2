from django.shortcuts import render
# take in json response
from django.http import JsonResponse
# serialize the json strings
from django.core.serializers import serialize
# need JSON
import json
# need the bird model
from birds.models import Bird
# need the view class to be inherited
from django.views import View
# grab the body of the request
from birds.helpers import GetBody

# Create your views here.

# Class for "/bird/"
class Bird_View(View):
    # INDEX route(GET to /bird/)
    def get(self, request):
        # GET all the birds
        all = Bird.objects.all()
        # grab all objects and turn into json string ~ serialize
        serialized = serialize("json", all)
        # veriable to serialize
        Final_Data = json.loads(serialized)
        # return the GET request
        return JsonResponse(Final_Data, safe=False)
    
    # CREATE route (POST to /bird/)
    def post(self, request):
        # grab the request body
        body = GetBody(request)
        # create the bird
        bird = Bird.objects.create(
            name = body["name"],
            breed = body["breed"],
            age = body["age"],
            size = body["size"],
            color = body["color"]
        )
        # serialize
        Final_Data = json.loads(serialize("json", [bird]))
        # return the bird
        return JsonResponse(Final_Data, safe=False)
    
# Class for "/bird/<id>/"
class Bird_View_ID(View):
    # Show route(GET to /bird/<id>/)
    def get(self, request, id):
        # get bird by id
        bird = Bird.objects.get(id=id)
        # variable to serialize
        Final_Data = json.loads(serialize("json", [bird]))
        # return the birdie
        return JsonResponse(Final_Data, safe=False)
        
    # Update route(PUT to /bird/<id>)
    def put(self, request, id):
        # grab the body of the ID
        body = GetBody(request)
        # grab the bird with spot operator and update the body
        Bird.objects.filter(id=id).update(**body)
        # query the updated bird
        bird = Bird.objects.get(id=id)
        # serialize
        Final_Data = json.loads(serialize("json", [bird]))
        # return the burb
        return JsonResponse(Final_Data, safe=False)
    
    # Delete route(DELETE to /bird/<id>
    def delete(self, request, id):
        # query the dog by ID so we can delete
        bird = Bird.objects.get(id=id)
        # delete the bird
        bird.delete()
        # serialize the response
        Final_Data = json.loads(serialize("json", [bird]))
        # return the response
        return JsonResponse(Final_Data, safe=False)