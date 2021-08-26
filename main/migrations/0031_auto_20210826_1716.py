# Generated by Django 3.2.6 on 2021-08-26 22:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_alter_curso_curso_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='image',
            field=models.ImageField(default=1, upload_to='albums/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='curso',
            name='curso_publicado',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 17, 16, 12, 441632), verbose_name='Fecha de publicación'),
        ),
    ]