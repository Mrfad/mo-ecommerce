# Generated by Django 3.2.9 on 2021-11-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20211128_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='unit_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]