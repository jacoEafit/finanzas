# Generated by Django 4.1.3 on 2022-12-20 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahorros', '0005_inversion_valor_inversion'),
    ]

    operations = [
        migrations.AddField(
            model_name='inversion',
            name='ROI',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='inversion',
            name='fecha_creacion',
            field=models.DateField(default=datetime.datetime(2022, 12, 20, 20, 31, 10, 682824, tzinfo=datetime.timezone.utc)),
        ),
    ]
