# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_center', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField()),
                ('good', models.ForeignKey(to='goods.GoodsInfo')),
                ('user', models.ForeignKey(to='user_center.UserInfo')),
            ],
        ),
    ]
