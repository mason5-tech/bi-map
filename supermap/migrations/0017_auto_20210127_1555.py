# Generated by Django 3.1.5 on 2021-01-27 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermap', '0016_lianjiadaqu_coordinate_shiyedaqu_coordinate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lianjiadaqu_coordinate',
            name='coordinateFkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermap.lianjiadaqu'),
        ),
        migrations.AlterField(
            model_name='shiyedaqu_coordinate',
            name='coordinateFkey',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermap.shiyedaqu'),
        ),
    ]
