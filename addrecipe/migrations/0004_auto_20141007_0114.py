# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addrecipe', '0003_remove_instruction_instruction_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(max_length=10, choices=[('TSP', 'tsp'), ('TBSP', 'tbsp'), ('CUP', 'cup'), ('QT', 'quart'), ('PT', 'pint'), ('L', 'liters'), ('GALLON', 'gallon'), ('G', 'grams'), ('LBS', 'lbs'), ('MLS', 'mLs')]),
        ),
    ]
