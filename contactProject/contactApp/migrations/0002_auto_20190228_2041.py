# Generated by Django 2.2 on 2019-02-28 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='Name',
            new_name='name',
        ),
    ]
