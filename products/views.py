from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory
from .models import Basket
from users.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'products/index.html', context)
    
def products(request, category_id=None, page_number=1):

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_number)

    context = {
        'title': 'Catalog',
        'products': products_paginator,
        'categorys': ProductCategory.objects.all(),                                          
    }
    return render(request, 'products/products.html', context)


def basket_add(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        baskets = Basket.objects.filter(user=request.user, product=product)
        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=1)
        else:
            basket = baskets.first()
            basket.quantity += 1
            basket.save()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(reverse('users:login'))


def basket_remove(request, basket_id):
    if request.user.is_authenticated:
        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        return HttpResponseRedirect(reverse('users:login'))

