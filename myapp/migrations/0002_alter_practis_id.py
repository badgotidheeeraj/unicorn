# Generated by Django 4.2.6 on 2023-12-25 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='practis',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
