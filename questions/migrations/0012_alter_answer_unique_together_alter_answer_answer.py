# Generated by Django 4.1.7 on 2023-04-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_alter_answer_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer',
            field=models.TextField(blank=True),
        ),
    ]
