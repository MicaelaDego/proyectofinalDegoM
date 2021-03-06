# Generated by Django 4.0.3 on 2022-04-30 16:59

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appblog', '0007_alter_post_cuerpo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=1000)),
                ('subtitulo', models.CharField(max_length=1000)),
                ('introduccion', models.CharField(max_length=4000)),
                ('cuerpo', ckeditor.fields.RichTextField()),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
            ],
        ),
    ]
