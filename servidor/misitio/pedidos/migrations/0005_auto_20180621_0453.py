# Generated by Django 2.0.6 on 2018-06-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20180621_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.TextField(max_length=70, null=True),
        ),
    ]