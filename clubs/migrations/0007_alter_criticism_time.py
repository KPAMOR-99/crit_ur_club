# Generated by Django 5.2 on 2025-07-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0006_remove_criticism_club_criticism_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='criticism',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
