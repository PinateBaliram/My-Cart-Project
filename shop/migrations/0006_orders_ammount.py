# Generated by Django 2.2.7 on 2020-07-31 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ammount',
            field=models.IntegerField(default=0),
        ),
    ]
