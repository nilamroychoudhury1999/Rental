# Generated by Django 3.0.7 on 2020-06-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birth_date',
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(default='lucknow', max_length=50),
            preserve_default=False,
        ),
    ]
