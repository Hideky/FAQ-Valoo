# Generated by Django 2.1.2 on 2018-10-09 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]