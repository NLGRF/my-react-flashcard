# Generated by Django 2.2.6 on 2019-11-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(blank=True, default='', max_length=100)),
                ('th', models.CharField(blank=True, default='', max_length=100)),
                ('ch', models.CharField(blank=True, default='', max_length=100)),
                ('category', models.CharField(blank=True, default='', max_length=100)),
                ('user', models.CharField(blank=True, default='', max_length=100)),
            ],
        ),
    ]
