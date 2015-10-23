# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatsat', '0002_auto_20151021_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatsat',
            name='meal_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='eatsat',
            name='wait_time',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
