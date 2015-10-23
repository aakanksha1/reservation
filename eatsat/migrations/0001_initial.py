# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('account_id', models.PositiveIntegerField()),
                ('points', models.PositiveIntegerField()),
                ('payment_info', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EatsAt',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('party_size', models.PositiveIntegerField()),
                ('wait_time', models.PositiveIntegerField()),
                ('meal_time', models.DateTimeField()),
                ('account', models.ForeignKey(to='eatsat.Account')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('estimated_wait_time', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='eatsat',
            name='restaurant',
            field=models.ForeignKey(to='eatsat.Restaurant'),
        ),
    ]
