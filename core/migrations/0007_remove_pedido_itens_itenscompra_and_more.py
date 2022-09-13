# Generated by Django 4.1 on 2022-09-12 19:50

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_ped_pro_pedido_itens_ped_pro_pedido_ped_pro_produto_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedido",
            name="itens",
        ),
        migrations.CreateModel(
            name="ItensCompra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("qtd_produto", models.IntegerField(default=1)),
                ("data_entrada", models.DateTimeField(default=datetime.datetime.now)),
                (
                    "pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="itens",
                        to="core.pedido",
                    ),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="core.produto",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="avaliacao",
            name="produto_avaliado",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="avaliacoes",
                to="core.itenscompra",
            ),
        ),
        migrations.DeleteModel(
            name="Ped_Pro",
        ),
    ]