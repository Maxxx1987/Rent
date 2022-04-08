# Generated by Django 4.0 on 2022-04-08 19:58

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('comparison', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comparison',
            name='product',
        ),
        migrations.RemoveField(
            model_name='comparison',
            name='product_info',
        ),
        migrations.AddField(
            model_name='comparison',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comparison',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]