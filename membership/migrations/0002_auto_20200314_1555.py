# Generated by Django 2.2.2 on 2020-03-14 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='is_member',
            new_name='membership',
        ),
    ]
