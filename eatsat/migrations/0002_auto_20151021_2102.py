# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatsat', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='points',
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(max_length=200, default='blah'),
            preserve_default=False,
        ),
    ]
