from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import product,Contact,Orders,OrderUpdate,Signup
from math import ceil
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
def mac_index(request):
    return render(request,"mac_index.html")

def index(request):
    allProds = []
    catprods = product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(product_category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params={'allProds':allProds}
    return render(request,"index.html",params)

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')

        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
    return render(request,"contact.html")

def view_cart(request):

    products=product.objects.all().values()
    #products=list(products1)
    #products=json.dumps(products1, cls=DjangoJSONEncoder)
    params={"products":list(products)}
    return render(request,"view_cart.html",params)




def searchMatch(query, item):
    if query.lower() in item.product_desc.lower() or query in item.product_name.lower() or query in item.product_category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = product.objects.values('product_category', 'id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prodtemp = product.objects.filter(product_category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]

        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg": ""}
    if len(allProds) == 0 or len(query)<4:
        params = {'msg': "Please make sure to enter relevant search query"}
    return render(request, 'search.html', params)



def productview(request,myid):
    product1=product.objects.filter(id=myid)


    return render(request,"products.html",{'product':product1[0]})

def checkout(request):
    if request.method=="POST":
        json_data=request.POST.get('json_data')
        ammount=request.POST.get('ammount')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        address1=request.POST.get('address1')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip')

        order=Orders(name=name,email=email,phone=phone,address=address,address1=address1,city=city,state=state,zip_code=zip_code,json_data=json_data,ammount=ammount)
        order.save()

        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()

        thank=True
        id=order.order_id
        return render(request,"checkout.html",{'thank':thank,'id':id})

    return render(request,"checkout.html")

def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].json_data],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')


    return render(request,"tracker.html")


def signup(request):
    #product1=product.objects.filter(id=myid)
    if request.method=="POST":
        email=request.POST.get('email')
        username=request.POST.get("uname")
        password=request.POST.get('psw')
        user=Signup(email=email,username=username,password=password)
        user.save()
    return render(request,"signup.html")

def login(request):
    #product1=product.objects.filter(id=myid)
    if request.method=="POST":
        username=request.POST.get("uname")
        password=request.POST.get('psw')
        users=Signup.objects.filter(username=username)
        for user in users:
            if user.username==username and user.password==password:
                return redirect("/shop/")
        else:
            return redirect("/login/")

    return render(request,"login.html")
