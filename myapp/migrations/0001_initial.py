# Generated by Django 4.2.6 on 2023-12-23 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='practis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('compony', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('pin', models.CharField(max_length=50)),
            ],
        ),
    ]
