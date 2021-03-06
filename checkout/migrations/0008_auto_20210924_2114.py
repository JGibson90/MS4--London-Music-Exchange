# Generated by Django 3.2.6 on 2021-09-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0007_alter_orderlineitem_product_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="delivery_cost",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name="order",
            name="grand_total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name="order",
            name="order_total",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]
