# Generated by Django 3.1.4 on 2021-01-18 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='test',
            field=models.TextField(null=True),
        ),
    ]
