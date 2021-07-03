from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    ram = {'a' : 'b' , 'c' : 'd'}
    return render (request,'index2.html')

def task1(request):
    djtext = request.GET.get('text','default')
    sjtext = "aaaa"
    final = sjtext + djtext
    return HttpResponse(final)

def ex1(request):
    return render (request,'sex.html')



