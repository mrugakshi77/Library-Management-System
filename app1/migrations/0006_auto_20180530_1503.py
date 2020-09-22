# Generated by Django 2.0.4 on 2018-05-30 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20180530_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='subject',
            field=models.CharField(default='subject', max_length=50),
        ),
        migrations.AlterField(
            model_name='books',
            name='no_of_copies',
            field=models.IntegerField(max_length=50),
        ),
    ]
