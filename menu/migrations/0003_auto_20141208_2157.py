# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20141208_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
