# Generated by Django 3.2.6 on 2021-08-26 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20210826_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 18, 45, 36, 600141), verbose_name='Fecha de publicación'),
        ),
    ]
