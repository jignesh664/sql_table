from django.shortcuts import render,redirect
from .models import Customer,Product,Order
# Create your views here.

def index(request):
    c=Customer.objects.all()
    params={'c':c}
    return render (request,'index1.html',params)



