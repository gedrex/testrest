# coding: utf-8
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.http import HttpResponse

from .models import Product, Type, List
# Create your views here.

def index(request):
    lists = get_list_or_404(List)
    return render(request, 'jidelni_listek/index.html', {
        'lists': lists,
    })

def detail(request, list_id):
    current_list = get_list_or_404(List, pk=list_id) 
    list_id = list_id
    current_list_name = current_list[0]
    products_by_type = Product.objects.filter(lists__id=list_id).all().order_by('product_type', 'product_order')

    return render(request, 'jidelni_listek/detail.html', {
        'current_list': current_list,
        'list_id': list_id,
        'current_list_name': current_list_name,
        'products_by_type' : products_by_type,
    })

