# Generated by Django 4.1.5 on 2023-02-17 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_person_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
