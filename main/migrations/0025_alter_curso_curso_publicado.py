# Generated by Django 3.2.6 on 2021-08-20 22:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 20, 17, 53, 37, 260458), verbose_name='Fecha de publicación'),
        ),
    ]
