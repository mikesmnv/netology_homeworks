# Generated by Django 3.1.2 on 2021-01-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210124_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcollection',
            name='name',
            field=models.CharField(max_length=25),
        ),
    ]