# Generated by Django 5.2.2 on 2025-06-08 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0008_character'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='anime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='characters', to='anime.anime'),
        ),
    ]
