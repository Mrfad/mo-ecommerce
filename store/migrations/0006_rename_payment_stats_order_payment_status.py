# Generated by Django 3.2.9 on 2021-11-12 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211107_1706'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='payment_stats',
            new_name='payment_status',
        ),
    ]