# Generated by Django 3.2.20 on 2023-08-11 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewsMessage',
        ),
        migrations.DeleteModel(
            name='Subscribers',
        ),
    ]