from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, render_to_response
import os
import datetime
from django.utils import timezone
from django.template import RequestContext
from jidelni_listek.models import Product, Type, DailyProduct, List, PoledniMenu
from photologue.views import PhotoListView

from braces.views import JSONResponseMixin


class PhotoJSONListView(JSONResponseMixin, PhotoListView):

    def render_to_response(self, context, **response_kwargs):
        return self.render_json_object_response(context['object_list'],
                                                **response_kwargs)
 
def index(request):
    lists = get_list_or_404(List)
    polednimenu = get_list_or_404(PoledniMenu)
    products_by_type = {}    
    poledni_menu_stale = {}
    poledni_menu_weekly = {}
    poledni_menu_daily = {}
    for onelist in lists:
        list_id = onelist.id
        products_by_type[list_id] = Product.objects.filter(lists__id=list_id).filter(pub_date__lte=timezone.now()).all().order_by('product_type', 'product_order')
    
    date = datetime.date.today()
    start_week = date - datetime.timedelta(date.weekday())
    end_week = start_week + datetime.timedelta(5)

    for poledni in polednimenu:
        poledni_id = poledni.id
        poledni_menu_stale[poledni_id] = DailyProduct.objects.filter(valid_for_date__range=[start_week, end_week]).filter(dtype=1).all()
        poledni_menu_weekly[poledni_id] = DailyProduct.objects.filter(valid_for_date__range=[start_week, end_week]).filter(dtype=2).all()
        poledni_menu_daily[poledni_id] = DailyProduct.objects.filter(valid_for_date__range=[start_week, end_week]).filter(dtype=3).all().order_by('valid_for_date', 'ptype') 
         

    return render(request, 'home/index.html', {
        'lists': lists,
        'products_by_type' : products_by_type,
        'polednimenu' : polednimenu,
        'poledni_menu_stale' : poledni_menu_stale,
        'poledni_menu_weekly': poledni_menu_weekly,
        'poledni_menu_daily': poledni_menu_daily,
        'start_week' : start_week,
        'end_week': end_week,
    })
        

# Create your views here.

