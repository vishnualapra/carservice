# Generated by Django 2.2.6 on 2019-10-13 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('manufacturer_code', models.AutoField(primary_key=True, serialize=False)),
                ('manufacturer_name', models.CharField(max_length=100)),
                ('manufacturer_detail', models.TextField()),
            ],
        ),
    ]