# Generated by Django 3.2.19 on 2024-03-07 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0003_auto_20240305_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='useraddress',
            field=models.TextField(null=True),
        ),
    ]
