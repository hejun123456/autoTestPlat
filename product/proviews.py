from django.shortcuts import render
from product.models import Products


# Create your views here.


def product_manage(request):
    username = request.session.get('user')
    product_list = Products.objects.all()
    print(product_list)
    return render(request, 'product_manage.html', {"user": username, "products": product_list})