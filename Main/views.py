from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *

def Home(request):
    Categorydata = Category.objects.all()
    context = {'category' : Categorydata}
    return render(request, "home/index.html" , context)

def Categories(request , id):
    category = Category.objects.get(pk=id)
    products = category.fooditem_set.all()
    context = {'fooditems': products} 
    return render(request, "category/category.html" , context)

def Product(request, id):
    product = FoodItem.objects.get(pk=id)
    context = {'fooditems': product}

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if request.user.is_authenticated:
            useraddress = request.POST.get('useraddress')
            total_price = product.price * quantity

            orderdata = Order.objects.create(
                user=request.user,
                useraddress=useraddress,
                order_date=timezone.now(),
                status='PENDING',
                total_price=total_price,
            )
            orderdata.save()

            order_item = OrderItem.objects.create(
                order=orderdata,
                food_item=product,
                quantity=quantity,
                price=total_price,
            )
            order_item.save()

            return redirect("Cart")
        else:
            return redirect('login')

    return render(request, "product/product.html", context)


def CartOrder(request):
    if request.user.is_authenticated:
        orders = request.user.order_set.prefetch_related('orderitem_set__food_item').order_by('-order_date')
        context = {'orders': orders}
        return render(request, "order/order.html", context)
    return render(request, "order/order.html")

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('userpassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            context = {'error_message': 'Invalid login credentials'}
            return render(request, "Login/Login.html", context)

    return render(request, "Login/Login.html")


def UserSignup(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        email = data.get('useremail') 
        password = data.get("userpassword")

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect("Login")
    
    return render(request, "Signup/Signup.html")

def UserLogout(request):
    logout(request)
    return redirect("/")
