# Generated by Django 3.1.5 on 2021-01-13 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermap', '0003_auto_20210112_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscircle',
            name='count_shops',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]