# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatsat', '0003_auto_20151022_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eatsat',
            name='meal_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='eatsat',
            name='wait_time',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
