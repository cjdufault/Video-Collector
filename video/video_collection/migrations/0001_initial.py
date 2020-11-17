# Generated by Django 3.1.3 on 2020-11-17 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=400)),
                ('notes', models.TextField(blank=True, null=True)),
                ('video_id', models.CharField(max_length=40, unique=True)),
            ],
        ),
    ]
