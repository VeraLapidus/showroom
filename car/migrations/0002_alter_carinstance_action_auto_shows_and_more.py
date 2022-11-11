# Generated by Django 4.1.2 on 2022-10-07 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auto_show', '0002_alter_autoshow_action_producers_and_more'),
        ('producer', '0001_initial'),
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinstance',
            name='action_auto_shows',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auto_show.actionautoshow', verbose_name='Акция автосалона'),
        ),
        migrations.AlterField(
            model_name='carinstance',
            name='action_producers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producer.actionproducer', verbose_name='Акция поставщика'),
        ),
    ]
