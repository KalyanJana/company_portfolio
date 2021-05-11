# Generated by Django 3.1.6 on 2021-04-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourproduct', '0002_auto_20210418_1328'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='product/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='product/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
