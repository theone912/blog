# Generated by Django 2.0.6 on 2018-06-13 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20180613_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
