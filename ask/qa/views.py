from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request, *args, **kwords):
    return HttpResponse('OK',status=200, content_type='text/plain')
