from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Products

# Create your views here.

def hi(request):
    products = Products.objects.all().values()
    template = loader.get_template('landpage.html')
    context = {
    'products': products,
    }
    return HttpResponse(template.render(context, request))

def about(request):
    template = loader.get_template('about.html')
    context ={}
    return HttpResponse(template.render(context, request))

def ptraining(request):
    template = loader.get_template('ptraining.html')
    context ={}
    return HttpResponse(template.render(context, request))

def details(request, id):
    product = Products.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {'product':product}
    return HttpResponse(template.render(context,request))