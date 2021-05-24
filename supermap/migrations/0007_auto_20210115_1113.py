# Generated by Django 3.1.5 on 2021-01-15 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermap', '0006_auto_20210115_1028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resblock',
            name='agreement_id',
        ),
        migrations.RemoveField(
            model_name='resblock',
            name='area',
        ),
        migrations.RemoveField(
            model_name='resblock',
            name='biz_type',
        ),
        migrations.RemoveField(
            model_name='resblock',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='resblock',
            name='deal_price',
        ),
        migrations.RemoveField(
            model_name='resblock',
            name='sign_date',
        ),
        migrations.RemoveField(
            model_name='resblock',
            name='subbiz_type',
        ),
        migrations.CreateModel(
            name='ResBlock_ST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_date', models.CharField(blank=True, max_length=20, null=True)),
                ('biz_type', models.CharField(blank=True, max_length=10, null=True)),
                ('subbiz_type', models.CharField(blank=True, max_length=20, null=True)),
                ('agreement_id', models.CharField(blank=True, max_length=20, null=True)),
                ('deal_price', models.FloatField(blank=True, default=0, null=True)),
                ('commission', models.FloatField(blank=True, default=0, null=True)),
                ('area', models.FloatField(blank=True, default=0, null=True)),
                ('block_STFkey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supermap.resblock')),
            ],
        ),
    ]
