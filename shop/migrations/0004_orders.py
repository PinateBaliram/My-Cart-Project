# Generated by Django 2.2.7 on 2020-07-29 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('json_data', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(default='', max_length=111)),
                ('email', models.CharField(default='', max_length=111)),
                ('phone', models.CharField(default='', max_length=12)),
                ('address', models.CharField(default='', max_length=5000)),
                ('address1', models.CharField(default='', max_length=5000)),
                ('state', models.CharField(default='', max_length=111)),
                ('city', models.CharField(default='', max_length=111)),
                ('zip_code', models.CharField(default='', max_length=111)),
            ],
        ),
    ]
