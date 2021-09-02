from django.core import serializers
from django.db.models import query
from django.db.models.expressions import F, Expression
from django.shortcuts import render,redirect
from .models import Customer,Product,Order
from django.http.response import Http404, HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.core.serializers import serialize

from django.contrib import messages





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
    records = Customer.objects.filter().values('state').distinct()
    records = [x['state'] for x in records]
    #citys =Customer.objects.filter().values('city')
    #citys=[y['city'] for y in citys]
    #print(records)
    params={'c':c,'o':o,'records': records}
    return render (request,'index.html',params)
   




@csrf_exempt
def getcity(request):
    if request.method=="POST":
        allConditions = ""
        city = request.POST.getlist('state[]')
        #print(city)
        finalCity = str(tuple(city)) if len(city) > 1 else str(tuple(city)).replace(',', '')
        if(city):
            allConditions += f"AND state IN {finalCity}" 

        querys=f" SELECT DISTINCT city FROM myapp_customer WHERE 1 = 1 {allConditions};"
        data=runsql(querys)
        #print(querys)
        #print(data)
        return JsonResponse({'status':'save','data':data}, safe = False)  
    else:
        return JsonResponse({'status':0})




#For Getting city from RoW Querys              
'''@csrf_exempt
def getcity(request):
    if request.method=="POST":
        allConditions = ""
        city = request.POST.getlist('state[]')
        print(city)
        finalCity = str(tuple(city)) if len(city) > 1 else str(tuple(city)).replace(',', '')
        if(city):
            allConditions += f"AND state IN {finalCity}" 

        querys=f" SELECT DISTINCT city FROM myapp_customer WHERE 1 = 1 {allConditions};"
        data=runsql(querys)
        print(querys)
        print(data)
        return JsonResponse({'status':'save','data':data}, safe = False)  
    else:
        return JsonResponse({'status':0})'''







'''@csrf_exempt
#Get data through ORM Methods
def getcity(request):
    if request.method=="POST":
        gtstate=Customer.objects.filter(state=request.POST['state'])
        finalCitys = []
        for i in gtstate:
            finalCitys.append({'city': i.city})
        #print(finalCitys)    
        return JsonResponse({'status':'save','finalCitys':finalCitys}, safe = False)  
        #return JsonResponse(serializers.serialize('json', gtcity), safe = False)
    else:
        return JsonResponse({'status':0})'''


#data get through using row querys 
@csrf_exempt
def getdata(request):
    if request.method == "POST":
        allConditions = ""
        

        state = request.POST.getlist('state[]')
        #print(state)
        #print(tuple(state))
        finalState = str(tuple(state)) if len(state) > 1 else str(tuple(state)).replace(',', '')
        if(state):
            allConditions += f"AND c.state IN {finalState}"


        city=request.POST.getlist('city[]')
        finalCity = str(tuple(city)) if len(city) > 1 else str(tuple(city)).replace(',', '')
        if(city):
            allConditions += f"AND c.city IN {finalCity}"

        #both date join throgh between in query
        tdate=request.POST['tdate']
        date=request.POST['fdate']
        if(date):
            allConditions += f"AND DATE(c.date) BETWEEN DATE('{date}') AND DATE('{tdate}')"

       
        querys=f"select c.fname, c.mobile, c.state, c.city, o.order_number, o.order_date, o.order_price, p.product_name, p.product_price from myapp_customer as c LEFT JOIN myapp_order as o ON c.id=o.id LEFT JOIN myapp_product as p ON p.id=c.id WHERE 1 = 1 {allConditions};"
        data=runsql(querys)      
        return JsonResponse({'status':'save','data':data}, safe = False)  
    else:
        return JsonResponse({'status':0 ,'message': 'Something went wrong.!'}, safe = False)


    
































'''# for using Row Querys
@csrf_exempt
def getdata(request):
    if request.method=="POST":

        allConditions = ""

        state = request.POST['state']
        if(state):
            allConditions += f"AND c.state = '{state}'"
        
        city = request.POST['city']
        if(city):
            allConditions += f"AND c.city = '{city}'"   

        email = request.POST['email']
        if(email):
            allConditions += f"AND c.email = '{email}'" 

        date = request.POST['date']
        if(date):
            allConditions += f"AND c.date = '{date}'"            

        querys=f"select c.fname, c.mobile, c.state, c.city, o.order_number, o.order_date, o.order_price, p.product_name, p.product_price from myapp_customer as c LEFT JOIN myapp_order as o ON c.id=o.id LEFT JOIN myapp_product as p ON p.id=c.id WHERE 1 = 1 {allConditions};"
        data=runsql(querys)
        #print(querys)
       
        return JsonResponse({'status':'save','data':data}, safe = False)  
    else:
        return JsonResponse({'status':0})
'''
























#Get Filter Method 
'''@csrf_exempt
def getdata(request):
    if request.method=="POST":
        stateCondition = ""
        state = request.POST['state']
        if(state):
            stateCondition += f"WHERE c.state = '{state}'"
        querys=f"select c.email, c.mobile from myapp_customer as c LEFT JOIN myapp_order as o ON c.id=o.id {stateCondition};"
        data=runsql(querys)
        #print(data)
        return JsonResponse({'status':'save','data':data}, safe = False)  
    else:
        return JsonResponse({'status':0})


for using ORM Quetys
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


