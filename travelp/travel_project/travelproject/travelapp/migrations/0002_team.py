# Generated by Django 4.2.6 on 2023-10-21 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('about', models.TextField()),
            ],
        ),
    ]
