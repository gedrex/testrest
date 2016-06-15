# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
import jidelni_listek.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('valid_for_date', models.DateTimeField(default=jidelni_listek.models.default_start_time, verbose_name=b'Platnost od', blank=True)),
                ('name', models.CharField(max_length=200, verbose_name=b'N\xc3\xa1zev')),
                ('amount', models.CharField(max_length=11, verbose_name=b'Mno\xc5\xbestv\xc3\xad', blank=True)),
                ('price', models.CharField(default=0, max_length=14, verbose_name=b'Cena', blank=True)),
                ('dtype', models.IntegerField(default=3, verbose_name=b'Nab\xc3\xaddka', choices=[(1, b'St\xc3\xa1l\xc3\xa1 nab\xc3\xaddka'), (2, b'T\xc3\xbddenn\xc3\xad nab\xc3\xaddka'), (3, b'Denn\xc3\xad nab\xc3\xaddka')])),
                ('ptype', models.IntegerField(default=4, verbose_name=b'Typ', choices=[(0, b'---'), (4, b'Pol\xc3\xa9vka'), (5, b'Hlavn\xc3\xad j\xc3\xaddlo')])),
            ],
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'N\xc3\xa1zev j\xc3\xaddeln\xc3\xadho l\xc3\xadstku')),
                ('list_short_description', models.CharField(max_length=100, verbose_name=b'Kr\xc3\xa1tk\xc3\xbd popis l\xc3\xadstku', blank=True)),
                ('list_long_description', models.TextField(verbose_name=b'Dlouh\xc3\xbd popis l\xc3\xadstku', blank=True)),
                ('icon', models.CharField(max_length=50, verbose_name=b'Ikona', choices=[(b'tree', b'Strom'), (b'cutlery', b'P\xc5\x99\xc3\xadbor'), (b'birthday-cake', b'Dort'), (b'heart', b'Srdce'), (b'coffee', b'Hrnek'), (b'glass', b'Sklenka'), (b'sun-o', b'Slunce'), (b'star', b'Hv\xc4\x9bzda'), (b'music', b'Hudba'), (b'hourglass-half', b'Poledne')])),
                ('bottom_line_description', models.TextField(verbose_name=b'Popis u spodn\xc3\xad \xc4\x8d\xc3\xa1sti menu', blank=True)),
                ('special', models.BooleanField(default=False, verbose_name=b'Speci\xc3\xa1ln\xc3\xad nab\xc3\xaddka')),
                ('experience', models.BooleanField(default=False, verbose_name=b'Z\xc3\xa1\xc5\xbeitkov\xc3\xa9 menu')),
                ('wine', models.BooleanField(default=False, verbose_name=b'Vinn\xc3\xbd list')),
                ('list_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
            ],
            options={
                'ordering': ['list_order'],
                'verbose_name': 'L\xedstek',
                'verbose_name_plural': 'L\xedstky',
            },
        ),
        migrations.CreateModel(
            name='PoledniMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'Poledn\xc3\xad menu', max_length=30, verbose_name=b'Poledn\xc3\xad menu')),
                ('list_long_description', models.TextField(verbose_name=b'Dlouh\xc3\xbd popis l\xc3\xadstku', blank=True)),
                ('icon', models.CharField(max_length=50, verbose_name=b'Ikona', choices=[(b'hourglass-half', b'Poledne'), (b'cutlery', b'P\xc5\x99\xc3\xadbor')])),
                ('bottom_line_description', models.TextField(verbose_name=b'Popis u spodn\xc3\xad \xc4\x8d\xc3\xa1sti menu', blank=True)),
            ],
            options={
                'verbose_name': 'Poledn\xed menu',
                'verbose_name_plural': 'Poledn\xed menu',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=200, verbose_name=b'N\xc3\xa1zev')),
                ('amount', models.CharField(max_length=11, verbose_name=b'Mno\xc5\xbestv\xc3\xad')),
                ('product_price', models.CharField(default=0, max_length=14, verbose_name=b'Cena')),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2016, 3, 23, 21, 5, 46, 346360, tzinfo=utc), verbose_name=b'Platnost od')),
                ('product_description', models.TextField(verbose_name=b'Popis', blank=True)),
                ('product_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('lists', models.ManyToManyField(to='jidelni_listek.List', verbose_name=b'Pat\xc5\x99\xc3\xad do l\xc3\xadstku', blank=True)),
                ('plist', models.ForeignKey(related_name='+', default=b'', blank=True, to='jidelni_listek.Product', null=True, verbose_name=b'Doporu\xc4\x8den\xc3\xa9 pivo')),
            ],
            options={
                'ordering': ['product_order'],
                'verbose_name': 'Produkt',
                'verbose_name_plural': 'Produkty',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'N\xc3\xa1zev')),
                ('type_order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('lists', models.ManyToManyField(to='jidelni_listek.List', verbose_name=b'L\xc3\xadstky', blank=True)),
                ('products', models.ManyToManyField(to='jidelni_listek.Product', verbose_name=b'Produkty', blank=True)),
            ],
            options={
                'ordering': ['type_order'],
                'verbose_name': 'Kategorie',
                'verbose_name_plural': 'Kategorie',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(verbose_name=b'Typ', blank=True, to='jidelni_listek.Type'),
        ),
        migrations.AddField(
            model_name='product',
            name='vlist',
            field=models.ForeignKey(related_name='+', default=b'', blank=True, to='jidelni_listek.Product', null=True, verbose_name=b'Doporu\xc4\x8den\xc3\xa9 v\xc3\xadno'),
        ),
        migrations.AddField(
            model_name='list',
            name='products',
            field=models.ManyToManyField(to='jidelni_listek.Product', blank=True),
        ),
        migrations.AddField(
            model_name='list',
            name='types_in_list',
            field=models.ManyToManyField(to='jidelni_listek.Type'),
        ),
        migrations.AddField(
            model_name='dailyproduct',
            name='poledni_menu',
            field=models.ForeignKey(default=1, to='jidelni_listek.PoledniMenu'),
        ),
    ]
