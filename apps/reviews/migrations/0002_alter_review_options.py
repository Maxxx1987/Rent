# Generated by Django 4.0 on 2022-03-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('-created_at',), 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]
