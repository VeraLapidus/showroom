# Generated by Django 4.1.4 on 2022-12-27 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_show', '0007_alter_actionautoshow_options_alter_autoshow_options_and_more'),
        ('customer', '0007_alter_customer_options_customer_owner_and_more'),
        ('producer', '0006_alter_actionproducer_options_and_more'),
        ('car', '0004_remove_carinstance_action_auto_shows_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelOptions(
            name='carinstance',
            options={'ordering': ['name'], 'verbose_name': 'Car Instance', 'verbose_name_plural': 'Car Instances'},
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='car',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='auto_shows',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='auto_shows', to='auto_show.autoshow'),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='condition',
            field=models.CharField(choices=[('Wish for AutoShow', 'WISH_AUTO_SHOW'), ('Wish for Customer', 'WISH_CUSTOMER'), ('At AutoShow', 'AT_AUTO_SHOW'), ('At Producer', 'AT_PRODUCER'), ('At Customer', 'AT_CUSTOMER')], max_length=60),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='customers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='customer.customer'),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_instances', to='car.car'),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='producers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='producers', to='producer.producer'),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
