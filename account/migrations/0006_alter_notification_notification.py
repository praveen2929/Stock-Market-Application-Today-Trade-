# Generated by Django 4.1.7 on 2023-03-24 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='notification',
            field=models.CharField(max_length=500),
        ),
    ]
