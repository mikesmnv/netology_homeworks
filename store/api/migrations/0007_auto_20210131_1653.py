# Generated by Django 3.1.2 on 2021-01-31 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210131_1505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderposition',
            old_name='order_id',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='orderposition',
            old_name='product_id',
            new_name='product',
        ),
    ]
