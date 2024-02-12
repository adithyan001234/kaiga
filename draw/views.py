from django.shortcuts import render,redirect
from.models import *

# Create your views here.
def home(request):
    return render(request,'draw/home.html')
def sign(request):
    if request.method=='POST':
        name1=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        drw=Drawer(name=name1,email=email,password=password)
        drw.save()
        return redirect('draw:login')
        

    return render(request,'draw/sign.html')
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            draw=Drawer.objects.get(email=email,password=password)
            request.session['draw']=draw.id
            return redirect('draw:dashbord')
        except Drawer.DoesNotExist:
            return render(request,'draw/login.html',{'msg':'invalid username or password'})
#         if Drawer.objects.filter(email=email,password=password).exists():
#             return redirect('draw:dashbord')
    return render(request,'draw/login.html')
def dashbord(request):
    if 'draw' in request.session:
        return render(request,'draw/dashbord.html')
    else:
        return render(request,'draw/home.html')
def viewdrawings(request):
    d=Drawings.objects.all()
    if 'sell' in request.session:
        return render(request,'draw/viewdrawings.html',{'drawings':d})
    else:
        return render(request,'draw/home.html')
def adddrawings(request):
    if request.method=='POST':
        drawing=request.FILES['drawing']
        name=request.POST['name']
        price=request.POST['price']
        discription=request.POST['discription']
        cdraw=Drawings(drawing=drawing,name=name,price=price,discription=discription)
        cdraw.save()
    if 'sell' in request.session:
        return render(request,'draw/adddrawings.html')
    else:
        return render(request,'draw/home.html')


    return render(request,'draw/adddrawings.html')
def Slogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        try:
            draw=Seller.objects.get(username=username,password=password)
            request.session['sell']=draw.id
            return redirect('draw:adddrawings')
        except Seller.DoesNotExist:
        
        # if Seller.objects.filter(username=username,password=password).exists():
        #     return redirect('draw:adddrawings')
        # else:
           return render(request,'draw/slogin.html',{'msg':'invalid inputs'})
    return render(request,'draw/slogin.html')
def deletedraw(request,did):
    Drawings.objects.get(id=did).delete()
    return redirect('draw:viewdrawings')
def update(request,did):
    drw=Drawings.objects.get(id=did)
    if request.method=='POST':
        drawing1=request.FILES['drawing']
        name1=request.POST['name']
        price1=request.POST['price']
        discription1=request.POST['discription']

        drw.drawing=drawing1
        drw.name=name1
        drw.price=price1
        drw.discription=discription1
        drw.save()
    if 'sell' in request.session:
        return render(request,'draw/update.html')
    else:
        return render(request,'draw/home.html')
      
        
    return render(request,'draw/update.html',{'drw':drw})
def view(request):
    if 'draw' in request.session:
         drwr=Drawings.objects.all()
         return render(request,'draw/view.html',{'drw':drwr})
    else:
        return render(request,'draw/home.html')
   
def about(request):
    return render(request,'draw/about.html')

def add_to_cart(request,product_id):
 if 'draw' in request.session:
    if request.method=='POST':
        product=Drawings.objects.get(id=product_id)
        cart_item,created=Cart.objects.get_or_create(drawings=product)
        if not created:
            cart_item.quantity+=1
            cart_item.save()
    return redirect('draw:cart')
 else:
        return render(request,'draw/home.html')
def cart(request):
 if 'draw' in request.session:
    cart_items=Cart.objects.all()
    total_price=sum(item.drawings.price*item.quantity for item in cart_items)
    total_price_per_item=[]
    grand_total=0
    for item in cart_items:
        item_total=item.drawings.price*item.quantity
        total_price_per_item.append({'item':item,'total':'item_total'})
        grand_total+=item_total
      
    return render(request,'draw/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})
 else:
        return render(request,'draw/home.html')
def removefromcart(request,drawings_id):
 if 'draw' in request.session:
    drawings=Drawings.objects.get(id=drawings_id)
    cart_item=Cart.objects.get(drawings=drawings)
    cart_item.delete()
    return redirect('draw:cart')
 else:
        return render(request,'draw/home.html')
def payment(request):
 if 'draw' in request.session:
    return render(request,'draw/payment.html')
 else:
        return render(request,'draw/home.html')
def card(request):
 if 'draw' in request.session:
    return render(request,'draw/card.html')
 

def logout(request):
    if 'draw' in request.session:
        del request.session['draw']
        return redirect('draw:home')
    
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        sel=Seller(username=username,password=password)
        sel.save()
        return redirect('draw:slogin')
    return render(request,'draw/signup.html')