# Generated by Django 3.2.6 on 2023-06-22 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0004_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createuser',
            old_name='login_id',
            new_name='user',
        ),
    ]