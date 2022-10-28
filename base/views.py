from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

# CORS HEADERS
# create endpoint to return json data
def endpoint(request):
    data = {
        "slackUsername": 'Enoch Omosebi',
        "backend": True,
        "age": 19,
        "bio": "A developer climbing towards his set out goals. too professional . I'm your friendly everyday tech-bro feel free to reach out .A weeb by heart ."
    }
    response = JsonResponse(data)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response