# Generated by Django 5.0.4 on 2024-05-23 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('amazon_url', models.URLField(blank=True)),
                ('flipkart_url', models.URLField(blank=True)),
                ('good_reads_review', models.CharField(blank=True, max_length=10, null=True)),
                ('cover_image', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('amazon_url', models.URLField(blank=True)),
                ('flipkart_url', models.URLField(blank=True)),
                ('good_reads_review', models.CharField(blank=True, max_length=10, null=True)),
                ('cover_image', models.URLField(blank=True)),
            ],
        ),
    ]
