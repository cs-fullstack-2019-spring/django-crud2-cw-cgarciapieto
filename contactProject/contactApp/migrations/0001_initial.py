# Generated by Django 2.2 on 2019-02-28 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('PhoneNumber', models.IntegerField(max_length=9)),
            ],
        ),
    ]
