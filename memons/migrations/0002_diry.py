# Generated by Django 3.0.6 on 2020-05-22 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
            ],
        ),
    ]
