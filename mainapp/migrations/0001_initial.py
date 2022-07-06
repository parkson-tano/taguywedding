# Generated by Django 4.0.6 on 2022-07-06 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('table', models.CharField(max_length=100)),
                ('arrived', models.BooleanField(default=False)),
                ('arrival_time', models.DateTimeField()),
            ],
        ),
    ]
