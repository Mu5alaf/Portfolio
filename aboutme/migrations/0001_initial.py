# Generated by Django 5.0 on 2023-12-28 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('position', models.CharField(max_length=30)),
                ('about', models.TextField(max_length=300, null=True)),
                ('picture', models.ImageField(blank=True, help_text='Upload an image file (JPEG, PNG, etc.)', null=True, upload_to='media')),
            ],
        ),
    ]
