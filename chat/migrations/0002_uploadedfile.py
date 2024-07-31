# Generated by Django 5.0.7 on 2024-07-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('original_name', models.CharField(max_length=255)),
                ('hash', models.CharField(max_length=32, unique=True)),
            ],
        ),
    ]