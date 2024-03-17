# We are creating the file because django wasn't made for creating APIs

# Below is a function so that we can take in the request. Must be decoded into utf8 ~ it would previously of been raw binary
# You then decode to utf8 and parses it into json


## Library for working with json
import json

def GetBody(request):
    # decode the request body into a unicode string
    unicode = request.body.decode('utf-8')
    # turn the unicode string into a python dictionary
    return json.loads(unicode)