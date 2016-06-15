# coding=utf-8 
from django.contrib import admin
from django.shortcuts import get_list_or_404

from adminsortable.admin import SortableAdmin

# Register your models here.

from .models import Product, List, Type, PoledniMenu, DailyProduct 

class ProductAdmin(SortableAdmin):
    
    list_display = ('amount', 'product_name', 'product_price', 'product_type')
    fields = (('amount', 'product_name', 'product_price'),('lists', 'product_type'),('plist', 'vlist'), 'pub_date', 'product_description')

    
    #    fieldsets = (
#        (None, {
#            'fields': (('amount', 'product_name', 'product_price', 'get_plist',)),
#        }),
#        ('Advanced options', {
#            'fields': ('lists', 'types', 'pub_date'),
#        }),
#    )
    
#    list_display = ('product_name', 'amount', 'product_price')
#
admin.site.register(Product, ProductAdmin)

class ListAdmin(SortableAdmin):
    fields = (('name', 'icon', 'list_short_description'),('special', 'experience', 'wine'), ('list_long_description', 'bottom_line_description'), ('types_in_list', 'products'))

admin.site.register(List, ListAdmin)

class TypeAdmin(SortableAdmin):

    fields = ('name', 'products', 'lists') 

admin.site.register(Type, TypeAdmin)


class DailyProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(DailyProduct, DailyProductAdmin)

class DailyProductInline(admin.StackedInline):
    model = DailyProduct
    extra = 0 

class PoledniMenuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ('name', 'icon')}),
        ('Popisky',              {'fields': [('list_long_description', 'bottom_line_description')], 'classes': ['collapse']}),
    ]
    inlines = [DailyProductInline]
    
admin.site.register(PoledniMenu, PoledniMenuAdmin)

