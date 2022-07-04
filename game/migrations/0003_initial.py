# Generated by Django 4.0.3 on 2022-05-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('game', '0002_delete_random'),
    ]

    operations = [
        migrations.CreateModel(
            name='Signin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=500)),
                ('email', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
