# Generated by Django 2.2.16 on 2021-12-19 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_cart_session_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
