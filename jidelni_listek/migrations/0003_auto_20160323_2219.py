# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jidelni_listek', '0002_auto_20160323_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 21, 19, 5, 63096, tzinfo=utc), verbose_name=b'Platnost od'),
        ),
    ]
