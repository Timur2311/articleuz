# Generated by Django 4.0.6 on 2022-07-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='update_count',
            field=models.IntegerField(default=0),
        ),
    ]
