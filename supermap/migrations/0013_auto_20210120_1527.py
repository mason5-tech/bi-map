# Generated by Django 3.1.5 on 2021-01-20 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supermap', '0012_auto_20210120_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resblock_st',
            name='sign_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
