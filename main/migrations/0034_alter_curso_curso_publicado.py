# Generated by Django 3.2.6 on 2021-08-26 22:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 17, 47, 59, 823713), verbose_name='Fecha de publicación'),
        ),
    ]
