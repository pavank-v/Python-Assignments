# Generated by Django 5.0.4 on 2024-05-05 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='amazon_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='flipkart_url',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='book',
            name='good_reads_review',
            field=models.FloatField(null=True),
        ),
    ]
