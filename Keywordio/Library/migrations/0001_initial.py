# Generated by Django 4.0.5 on 2022-07-07 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=500)),
                ('Writer', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('name', models.CharField(max_length=500)),
                ('userName', models.CharField(max_length=500, primary_key=True, serialize=False)),
                ('position', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=1000)),
                ('salt', models.CharField(max_length=1000)),
            ],
        ),
    ]
