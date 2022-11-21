# Generated by Django 4.1.3 on 2022-11-21 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0005_alter_producer_name'),
        ('deals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='participants',
            field=models.CharField(choices=[('Поставщик-автосалон', 'PRODUCER_SHOWROOM'), ('Автосалон-покупатель', 'SHOWROOM_CUSTOMER')], max_length=50, verbose_name='Стороны сделки'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='producers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producer.producer', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='deal',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
