# Generated by Django 3.0.8 on 2020-07-15 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20200715_1908'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='curr_partner',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='rate',
            name='feel',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
