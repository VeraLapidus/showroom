# Generated by Django 4.1.3 on 2022-11-22 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_show', '0005_alter_autoshow_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoshow',
            name='wish_car',
            field=models.TextField(blank=True, default='{"brand": "None", "model": "None", "year": "None", "color": "None", "price": "None"}', null=True),
        ),
    ]
