from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vista2(request):
    html="""
    <h1 style='color:green'>
    Evaluacion
    Miedo
    Terror
    Pánico
    </h1>"""
    return HttpResponse(html)