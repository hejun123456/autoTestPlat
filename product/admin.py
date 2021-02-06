from django.contrib import admin
from product.models import Products
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname', 'productdesc', 'producter', 'id', 'create_time', 'update_time']


admin.site.register(Products, ProductAdmin)
