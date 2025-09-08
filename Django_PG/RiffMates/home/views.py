from django.shortcuts import render
from django.http import HttpResponse

def credits(request):
    content = "Nicky\nSunil"

    return HttpResponse(content, content_type="text/plain")