# Generated by Django 2.0.6 on 2018-06-21 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_auto_20180619_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.TextField(null=True),
        ),
    ]
