# Generated by Django 4.2 on 2024-04-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPages', '0005_alter_torta_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='torta',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='torta',
            name='price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='torta',
            name='visit_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
