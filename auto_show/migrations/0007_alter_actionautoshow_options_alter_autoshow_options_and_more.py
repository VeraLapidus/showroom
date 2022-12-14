# Generated by Django 4.1.4 on 2022-12-27 11:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auto_show', '0006_alter_autoshow_wish_car'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actionautoshow',
            options={'verbose_name': 'AutoShows action', 'verbose_name_plural': 'AutoShows actions'},
        ),
        migrations.AlterModelOptions(
            name='autoshow',
            options={'verbose_name': 'AutoShow', 'verbose_name_plural': 'AutoShows'},
        ),
        migrations.AlterModelOptions(
            name='discountautoshow',
            options={'verbose_name': 'AutoShows customer discount', 'verbose_name_plural': 'AutoShows customer discounts'},
        ),
        migrations.AddField(
            model_name='autoshow',
            name='owner',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='amount_action',
            field=models.PositiveIntegerField(verbose_name="Action's amount, %"),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='auto_shows',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_show.autoshow', verbose_name='Car showroom'),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='date_finish',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='date_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='actionautoshow',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='list_auto',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='list_customers',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='list_producers',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='autoshow',
            name='year_foundation',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='amount_discount',
            field=models.PositiveIntegerField(verbose_name="Discount's amount, %"),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='auto_shows',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_show.autoshow'),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='max_amount_spent',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name="Max purchase's amount for discount"),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='min_amount_spent',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name="Min purchase's amount for discount"),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='discountautoshow',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
