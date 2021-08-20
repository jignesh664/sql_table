from django.db.models import query
from django.shortcuts import render,redirect
from .models import Customer,Product,Order
from django.http.response import Http404, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.core.serializers import serialize





# Create your views here.

# for connect db
def runsql(q):
    cursor=connection.cursor()
    cursor.execute(q)
    if(cursor.description != None):
        columns=[col[0] for col in cursor.description] 
        return[
            dict(zip(columns,row))
            for row in cursor.fetchall()
        ] 
    else:
        return True



def index(request):
    c=Customer.objects.all()
    o=Order.objects.all()
    # for remove dublicates values 
    records =Customer.objects.filter().values('state').distinct()
    params={'c':c,'o':o,'records':records}
    return render (request,'index.html',params)


# for using Row Querys
@csrf_exempt
def getdata(request):
    if request.method=="POST":
        querys="select * from myapp_customer as c LEFT JOIN myapp_order as o ON c.id=o.id;"
        data=runsql(querys) 
        return JsonResponse({'status':'save','data':serialize('json',data)}, safe = False)  
    else:
        return JsonResponse({'status':0})


'''for using ORM Quetys
def getdata(request):
    if request.method=="POST":
        customers=Customer.objects.filter(state=request.POST['state'])
        #create list of all city data
        finaldata = []  
        # for i in orders:
        #     finaldata.append({'fname': i.fname, 'id': i.id})  
        return JsonResponse({'status':'save','finaldata':serialize('json', customers)}, safe = False)  
    else:
        return JsonResponse({'status':0})'''
          