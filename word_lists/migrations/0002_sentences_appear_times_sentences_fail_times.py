# Generated by Django 5.1.1 on 2024-09-25 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentences',
            name='appear_times',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='sentences',
            name='fail_times',
            field=models.IntegerField(null=True),
        ),
    ]
