# Generated by Django 4.0 on 2022-04-08 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_price'),
        ('comparison', '0002_remove_comparison_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComparisonProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comparison', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comparison.comparison')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
