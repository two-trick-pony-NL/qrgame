# Generated by Django 4.1.7 on 2023-04-17 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_answers'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
    ]
