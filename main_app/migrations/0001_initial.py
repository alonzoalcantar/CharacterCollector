# Generated by Django 4.1.4 on 2022-12-25 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('race', models.CharField(max_length=100)),
                ('background', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
                ('style', models.CharField(max_length=100)),
            ],
        ),
    ]
