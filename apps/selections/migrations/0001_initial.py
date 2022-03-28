# Generated by Django 4.0 on 2022-03-28 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('products', '0003_product_price'),
        ('catalog', '0002_alter_section_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='Цена')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.user')),
            ],
            options={
                'verbose_name': 'Подборка',
                'verbose_name_plural': 'Подборки',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='UserSelection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.section')),
                ('selection', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selections.selection')),
            ],
        ),
    ]