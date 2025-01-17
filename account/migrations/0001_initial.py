# Generated by Django 4.1.5 on 2023-02-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
                ('State', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
