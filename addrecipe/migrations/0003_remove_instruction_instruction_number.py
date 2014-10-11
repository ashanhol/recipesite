# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addrecipe', '0002_auto_20141006_1947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instruction',
            name='instruction_number',
        ),
    ]
