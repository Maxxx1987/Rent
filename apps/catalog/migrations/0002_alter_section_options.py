# Generated by Django 4.0 on 2022-03-23 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('order', 'slug'), 'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
