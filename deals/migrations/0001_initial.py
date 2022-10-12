# Generated by Django 4.1.2 on 2022-10-07 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto_show', '0001_initial'),
        ('customer', '0001_initial'),
        ('producer', '0001_initial'),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, verbose_name='Название сделки')),
                ('participants', models.CharField(choices=[('producer-showroom', 'поставщик-автосалон'), ('showroom-customer', 'автосалон-покупатель')], max_length=40, verbose_name='Стороны сделки')),
                ('price', models.PositiveIntegerField(verbose_name='Сумма сделки, USD')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата совершения сделки')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления сделки')),
                ('auto_shows', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auto_show.autoshow', verbose_name='Автосалон')),
                ('car_instances', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.carinstance', verbose_name='Авто')),
                ('customers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='Покупатель')),
                ('producers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producer.producer', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Сделка',
                'verbose_name_plural': 'Сделки',
                'ordering': ['name'],
            },
        ),
    ]