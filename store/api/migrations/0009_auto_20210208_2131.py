# Generated by Django 3.1.2 on 2021-02-08 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210131_1657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='productreview',
            name='id',
        ),
    ]
