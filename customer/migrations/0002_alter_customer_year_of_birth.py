# Generated by Django 4.1.2 on 2022-10-07 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='year_of_birth',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Год рождения'),
        ),
    ]