# Generated by Django 4.1.7 on 2023-04-17 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qrcodegame', '0002_alter_leaderboard_adam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='adam',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]