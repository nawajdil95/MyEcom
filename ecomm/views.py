from traceback import print_tb
from django.http import HttpResponse
from django.shortcuts import redirect, render
from sympy import re
# from tenacity import retry
# from validators import email

from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
from .models import register_info,product,Category,order


def index(request):
    if request.method =="POST":
        product_id = request.POST.get('cartid')
        remove=request.POST.get('minus')

        cart_id = request.session.get('cart')
        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id]=quantity-1
                else:
                    cart_id[product_id] = quantity +1
            else:
                cart_id[product_id] = 1
        else:
            cart_id ={}
            cart_id[product_id] = 1
        request.session['cart'] = cart_id
        # print(request.session['cart'])

    path = product.objects.all()
    cat = Category.objects.all()
    cat_id =request.GET.get('category')
    if cat_id:
        path = product.objects.filter(category_id=cat_id)
    else:
        path = product.objects.all()
    return render(request, 'home.html',{'path': path,'cate':cat})



    
      

    # try:
    #     c = request.session['email']
    #     if request.session['email']:
    #         username = register_info.objects.all()
    #     else:
    #         return render(request, 'home.html', {'c': c})
    # except:
    #     return render(request, 'home.html')

    return render(request, 'home.html', {'path':path,'cate':cat})


def contact(request):
    return render(request,'contact.html')


def save(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        gender = request.POST.get('gender')

        # fetch_info = register_info.objects.get(email=email)
        # if(fetch_info == email):

        save_info = register_info(firstname=fname, lastname=lname,
                                  mobile=mobile, password=password, gender=gender, email=email)
        save_info.save()

        return redirect('home')


def login(request):
    error_msg = None
    if request.method == "POST":
        emails = request.POST.get('email')
        # print(emails)
        try:
            fetch_email = register_info.objects.get(email=emails)
            # print(fetch_email)
            request.session['email'] = emails
            return redirect('home')
        except:
            error_msg = "invalid email"
            return render(request, 'contact.html', {'error_msg': error_msg})

        # c = register_info.getemail(emails)
        # print(c)
        # password = request.POST.get('password')

        # try:
        #
        #     print(fetch_info)
        #     # return fetch_info
        # except:
        #     return False
        # if fetch_info == emails:
        #     print("hhhhh")
        #     return HttpResponse("fetch_info")
        # else:
        #     return HttpResponse("byr")
        # # context = {
        # #     'fetch_info': fetch_info
        # # }

        return render(request, 'home.html')


def register(request):
    try:
        email = request.POST.get('email')
        fetch_email = register_info.objects.get(email=email)

        if (fetch_email.email == email):
            return HttpResponse('user already exist')
    except:

        if request.method == "POST":
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            mobile = request.POST.get('mobile')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            password = request.POST.get('password')
            print(password)

            store_data = register_info(firstname=fname, lastname=lname,
                                       mobile=mobile, gender=gender, email=email, password=make_password(password))

            store_data.save()

            return redirect('home')


def login_info(request):
    error_msg = None

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            fetch_email = register_info.objects.get(email=email)

            if (fetch_email.email == email):
                flag = check_password(password, fetch_email.password)
                if flag:
                    request.session['email'] = fetch_email.email
                    request.session['customer_id']=fetch_email.id
                    return redirect('home')
                else:
                    error_msg = "Please Enter valid password"
                    return render(request, 'home.html', {'error_msg': error_msg})
        except:
            error_msg = "Please Enter valid  Email"
            return render(request, 'home.html', {'error_msg': error_msg})

        return HttpResponse(fetch_email.email, fetch_email.password)


def logout(request):
    request.session.clear()
    return redirect('home')


def cart(request):
    ids=list(request.session.get('cart').keys())
    cart_pro=product.objects.filter(id__in=ids)
    # print(cart_pro)
    return render(request,'cart.html',{'cart_pro':cart_pro})
    # print(list(request.session.get('cart').keys))
    return render(request,'cart.html')
def checkout(request):
    if request.method=="POST":
        address=request.POST.get("address")
        mobile=request.POST.get("mobile")
        customer_id=request.session.get('customer_id')
        cart=request.session.get('cart')
        products=product.objects.filter(id__in=list(cart.keys()))
        print(products)
        for pro in products:
            save_order_dlts=order(
                customer=register_info(id=customer_id),
                price=pro.price,
                product = pro, 
                quantity=cart.get(str(pro.id)),
                address=address,
                phone=mobile   
                )
                # print(address,mobile,cart,customer_id,products)
            save_order_dlts.save()
            request.session['cart']={}
        return redirect('cart')
def order_dtl(request):
    customer=request.session.get('customer_id')
    ord_dtls=order.objects.filter(customer=customer).order_by('-date')
    return render(request,'order.html',{'ord_dtls':ord_dtls})           
            
                
            

    # return render(request,'order.html')
         
