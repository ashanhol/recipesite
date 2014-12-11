# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'items',
                'verbose_name': 'item',
                'ordering': ('menu',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('creation_date', models.DateTimeField(verbose_name='creation date')),
            ],
            options={
                'verbose_name_plural': 'menus',
                'verbose_name': 'menu',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='menu',
            field=models.ForeignKey(verbose_name='menu', to='menu.Menu'),
            preserve_default=True,
        ),
    ]
