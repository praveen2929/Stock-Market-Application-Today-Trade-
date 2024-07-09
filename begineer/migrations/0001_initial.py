# Generated by Django 4.1.7 on 2023-02-20 19:28

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('number', models.IntegerField(default=0)),
                ('image1', models.ImageField(default='static\\image\\email.png', upload_to='image')),
                ('desc', tinymce.models.HTMLField()),
            ],
        ),
    ]