# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addrecipe', '0004_auto_20141007_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='dairy_free',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='gluten_free',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='soy_free',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegan',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='vegetarian',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.FloatField(default=999.9),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(choices=[('TSP', 'tsp'), ('TBSP', 'tbsp'), ('CUP', 'cup'), ('QT', 'quart'), ('PT', 'pint'), ('L', 'liters'), ('GALLON', 'gallon'), ('G', 'grams'), ('LBS', 'lbs'), ('MLS', 'mLs'), ('OBJECT', 'of these')], max_length=10),
        ),
    ]
