# Generated by Django 2.0.6 on 2018-06-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='archivo_adjunto',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha',
            field=models.TextField(null=True),
        ),
    ]