# Generated by Django 4.0 on 2022-03-23 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_alter_order_identifier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='rent_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='rent_till',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
