# coding: utf-8

from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin

class Product(SortableMixin):
    product_name = models.CharField('Název', max_length=200)
    amount = models.CharField('Množství', max_length=11)
    product_price = models.CharField('Cena', default=0, max_length=14)
    lists = models.ManyToManyField('List', blank=True, verbose_name='Patří do lístku')
    product_type = models.ForeignKey('Type', blank=True, verbose_name='Typ')
    pub_date = models.DateTimeField('Platnost od', default=timezone.now())  
    plist = models.ForeignKey('self', related_name='+', blank=True, limit_choices_to={'product_type__name': 'Pivo'}, verbose_name='Doporučené pivo', null=True, default="")
    vlist = models.ForeignKey('self', related_name='+', blank=True, limit_choices_to={'product_type__name': 'Víno'}, verbose_name='Doporučené víno', null=True, default="")
    product_description = models.TextField('Popis', blank=True)

    # ordering field
    product_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)


    def __unicode__(self):
        return '%s (%s)' % (self.product_name, self.amount)

    class Meta:
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'
        ordering = ['product_order']



class Type(SortableMixin):
    name = models.CharField('Název', max_length=100)
    products = models.ManyToManyField(Product, verbose_name='Produkty', blank=True)
    lists = models.ManyToManyField('List', verbose_name='Lístky', blank=True)
    # ordering field
    type_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategorie'
        verbose_name_plural = 'Kategorie'
        ordering = ['type_order']

class List(SortableMixin):
    name = models.CharField('Název jídelního lístku', max_length=100)
    products = models.ManyToManyField(Product, blank=True, through=Product.lists.through)
    list_short_description = models.CharField('Krátký popis lístku', max_length=100, blank=True)
    list_long_description = models.TextField('Dlouhý popis lístku', blank=True)
    icon = models.CharField('Ikona', max_length=50, choices=(('tree', 'Strom'), ('cutlery', 'Příbor'), ('birthday-cake', 'Dort'), ('heart', 'Srdce'), ('coffee', 'Hrnek'), ('glass', 'Sklenka'), ('sun-o', 'Slunce'), ('star', 'Hvězda'), ('music', 'Hudba'), ('hourglass-half', 'Poledne')))
    bottom_line_description = models.TextField('Popis u spodní části menu', blank=True)
    types_in_list = models.ManyToManyField(Type)
    special = models.BooleanField('Speciální nabídka', default=False)
    experience = models.BooleanField('Zážitkové menu', default=False) 
    wine = models.BooleanField('Vinný list', default=False)
    
    # ordering field 
    list_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    @property
    def sorted_products(self):
        return self.products.all().order_by('product_type', 'product_order')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Lístek'
        verbose_name_plural = 'Lístky'
        ordering = ['list_order']

class PoledniMenu(models.Model):
    name = models.CharField('Polední menu', max_length=30, default='Polední menu')
    list_long_description = models.TextField('Dlouhý popis lístku', blank=True)
    icon = models.CharField('Ikona', max_length=50, choices=(('hourglass-half', 'Poledne'), ('cutlery', 'Příbor')))
    bottom_line_description = models.TextField('Popis u spodní části menu', blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Polední menu'
        verbose_name_plural = 'Polední menu'

def default_start_time():
        now = datetime.now()
        start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        return start if start > now else start + timedelta(days=1)

class DailyProduct(models.Model):
    poledni_menu = models.ForeignKey(PoledniMenu, default=1)
    valid_for_date = models.DateTimeField('Platnost od', default=default_start_time, blank=True)
    name = models.CharField('Název', max_length=200 )
    amount = models.CharField('Množství', max_length=11, blank=True)
    price = models.CharField('Cena', default=0, max_length=14, blank=True)
    NONE = 0
    SOUP = 4 
    BIGFOOD = 5 
    STALE = 1
    WEEKLY = 2
    DAILY = 3
    TIME_CHOICES = (
        (STALE, 'Stálá nabídka'),
        (WEEKLY, 'Týdenní nabídka'),
        (DAILY, 'Denní nabídka'),
    )
    FOOD_CHOICES = (
        (NONE, '---'),
        (SOUP, 'Polévka'),
        (BIGFOOD, 'Hlavní jídlo'),
    )
    dtype = models.IntegerField('Nabídka', choices=TIME_CHOICES, default=DAILY)
    ptype = models.IntegerField('Typ', choices=FOOD_CHOICES, default=SOUP)
    def __unicode__(self):
        return self.name

