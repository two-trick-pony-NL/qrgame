# Generated by Django 4.1.7 on 2023-04-17 19:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_delete_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]