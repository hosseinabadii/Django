# Generated by Django 4.2.1 on 2023-05-22 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_init'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User2',
            new_name='User',
        ),
    ]