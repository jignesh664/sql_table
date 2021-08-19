from django.shortcuts import render,redirect
from .models import Customer,Product,Order
from django.http.response import Http404, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def index(request):
    c=Customer.objects.all()
    o=Order.objects.all()
    params={'c':c,'o':o}
    return render (request,'index.html',params)

@csrf_exempt
def getorder(request):
    if request.method=="POST":
        customers=Customer.objects.all(id=request.POST['state_id'])
        orders=Order.objects.all()
    else:
        return redirect('/')





'''@csrf_exempt
def getorder1(request):
    if request.method=="POST":
        state=Customer.objects.get(id=request.POST['state_id'])
        orders=Order.objects.filter(state_id=state.id)
        alldetails=[]
        for i in orders:
            alldetails.append({'name':i.fname,'email':i.email,'mobile':i.mobile,'orderdate':i.order_date,'order_number':i.order_number})
            return JsonResponse({'alldetails':alldetails})
    else:
        return redirect('/')    '''       

            