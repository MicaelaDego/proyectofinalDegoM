# Generated by Django 4.0.3 on 2022-04-18 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('titulo', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('subtitulo', models.CharField(max_length=100)),
                ('introduccion', models.CharField(max_length=400)),
                ('cuerpo', models.CharField(max_length=2000)),
                ('autor', models.CharField(max_length=40)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
