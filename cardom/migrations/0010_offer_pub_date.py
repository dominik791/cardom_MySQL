# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cardom', '0009_auto_20150708_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name=b'Data publikacji'),
        ),
    ]
