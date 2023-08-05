import typing

from django.http import HttpRequest
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request: HttpRequest):
    return redirect('catalog')


def show_catalog(request: HttpRequest):
    template = 'catalog.html'
    phones: typing.List[Phone]

    type_sort = request.GET.get('sort', 'all')

    sorting_mode = {
        'all': Phone.objects.all(),
        'name': Phone.objects.order_by('name'),
        'min_price': Phone.objects.order_by('price'),
        'max_price': Phone.objects.order_by('-price'),
        }

    phones = sorting_mode.get(type_sort)

    context = {
        'phones': phones
    }

    return render(request, template, context)


def show_product(request: HttpRequest, slug):
    template = 'product.html'

    phone = Phone.objects.get(slug=slug)

    context = {
        'phone': phone
    }
    return render(request, template, context)
