# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20150902_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='content',
            field=models.TextField(default=b'hello'),
        ),
    ]
