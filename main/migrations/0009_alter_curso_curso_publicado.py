# Generated by Django 3.2.6 on 2021-08-19 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 17, 40, 21, 338717), verbose_name='Fecha de publicación'),
        ),
    ]
