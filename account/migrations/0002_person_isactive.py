# Generated by Django 4.1.5 on 2023-02-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='isactive',
            field=models.BooleanField(default=False),
        ),
    ]
