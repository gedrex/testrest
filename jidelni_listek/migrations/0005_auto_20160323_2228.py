# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jidelni_listek', '0004_auto_20160323_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 21, 28, 45, 590178, tzinfo=utc), verbose_name=b'Platnost od'),
        ),
    ]
