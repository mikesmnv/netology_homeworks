# Generated by Django 3.1.2 on 2021-01-31 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210126_1945'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['created_at'], 'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderposition',
            options={'verbose_name': 'Информация о заказе', 'verbose_name_plural': 'Информация о заказах'},
        ),
    ]
