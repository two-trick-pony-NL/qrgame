# Generated by Django 4.1.7 on 2023-04-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_alter_answer_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
