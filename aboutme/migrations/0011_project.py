# Generated by Django 5.0 on 2023-12-30 19:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0010_skills_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, help_text='Upload an image file (JPEG, PNG, etc.)', null=True, upload_to='project')),
                ('name', models.CharField(default='Your project ', max_length=255)),
                ('tools', models.CharField(default='Project tools', max_length=255)),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aboutme.info')),
            ],
        ),
    ]
