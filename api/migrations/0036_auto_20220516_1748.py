# Generated by Django 3.1.4 on 2022-05-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_remove_receiveitem_price_diff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
