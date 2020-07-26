from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Product

# Create your views here.


def index(request,):
    product = Product.objects.all()
    return render(request, 'products/index.html', {'product': product})


def detail_view(request, product_id):
    return HttpResponse(product_id)

