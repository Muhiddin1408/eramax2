# Generated by Django 3.1.4 on 2022-03-09 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20220309_1536'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DollarRate',
        ),
        migrations.AddField(
            model_name='cart',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
