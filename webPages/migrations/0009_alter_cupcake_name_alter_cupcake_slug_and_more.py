# Generated by Django 4.2 on 2024-04-20 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webPages', '0008_alter_cupcake_slug_alter_torta_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupcake',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='cupcake',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='torta',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
        migrations.AlterField(
            model_name='torta',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
