# Generated by Django 4.0.5 on 2022-06-08 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scrapes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scrapy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('location', models.TextField()),
                ('beds', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='ScrapyItem',
        ),
    ]