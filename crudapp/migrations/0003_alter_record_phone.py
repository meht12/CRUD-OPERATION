# Generated by Django 5.0.1 on 2024-01-15 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_alter_record_address_alter_record_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
