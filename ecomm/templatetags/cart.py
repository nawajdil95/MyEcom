from unicodedata import name
from django import template
from sympy import O
register=template.Library()
@register.filter(name = 'isexistincart')
def isexistincart(product,cart):
    keys = cart.keys()
    print(keys)
    for id in keys:
        if int(id) == product.id:
            return True
    return False

@register.filter(name = "cartquantity")
def cartquantity(product,cart):
        cart_id=cart.keys()
        for id in cart_id:
            if int(id) == product.id:
                return cart.get(id)
        return False


@register.filter(name="total_price") 
def total_price(product,cart):
    return product.price* cartquantity(product,cart)  



@register.filter(name="grand_total") 
def grand_total(products,cart): 
    sum=0
    for p in products:
        sum =+total_price(p,cart)
    return sum
@register.filter(name='multiplyprice') 
def multiplyprice(num1,num2):
    return num1*num2   


    
    
        



    
            


    

    

