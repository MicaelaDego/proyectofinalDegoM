# Generated by Django 4.0.3 on 2022-04-23 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appblog', '0004_alter_post_introduccion_alter_post_subtitulo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('mensaje', models.CharField(max_length=500, primary_key=True, serialize=False)),
            ],
        ),
    ]
