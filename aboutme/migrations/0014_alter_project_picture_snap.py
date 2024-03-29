# Generated by Django 5.0 on 2023-12-30 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0013_remove_project_picture_project_picture_snap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='picture_snap',
            field=models.ImageField(blank=True, help_text='Upload an image file (JPEG, PNG, etc.)', null=True, upload_to='media/project'),
        ),
    ]
