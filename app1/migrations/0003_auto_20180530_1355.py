# Generated by Django 2.0.4 on 2018-05-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Librarian', 'Librarian'), ('Student', 'Student')], default='Librarian', max_length=2),
        ),
    ]
