# Generated by Django 4.1 on 2022-11-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_alter_pedido_data_entrega"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pedido",
            name="qtd_parcela",
            field=models.IntegerField(null=True),
        ),
    ]
