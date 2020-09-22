# Generated by Django 2.0.4 on 2018-07-21 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_auto_20180530_1507'),
    ]

    operations = [
        migrations.CreateModel(
            name='requested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('no_of_copies', models.IntegerField()),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Reject', 'Reject'), ('Unavailable', 'Unavailable')], default='Available', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='no_of_copies',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='books',
            name='star_rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Librarian', 'Librarian'), ('Student', 'Student')], default='Librarian', max_length=10),
        ),
    ]
