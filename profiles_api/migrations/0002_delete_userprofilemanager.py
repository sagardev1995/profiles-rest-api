# Generated by Django 2.2 on 2022-11-18 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfileManager',
        ),
    ]