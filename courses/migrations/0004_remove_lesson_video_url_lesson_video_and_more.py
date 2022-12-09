# Generated by Django 4.1.3 on 2022-12-09 00:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_exercises_answer_alter_exercises_answer_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='video_url',
        ),
        migrations.AddField(
            model_name='lesson',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='thumbnail'),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='answer_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='answer_image'),
        ),
        migrations.AlterField(
            model_name='exercises',
            name='question_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='question_image'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='thumbnail'),
        ),
    ]