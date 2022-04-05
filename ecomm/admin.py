from django.contrib import admin
# from numpy import product

from .models import register_info,product,Category,order
# Register your models here.


class register_dtls(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']


admin.site.register(register_info, register_dtls)
admin.site.register(product)
admin.site.register(Category)
admin.site.register(order)