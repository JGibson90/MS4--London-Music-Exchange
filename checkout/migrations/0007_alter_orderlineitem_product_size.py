# Generated by Django 3.2.6 on 2021-09-24 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0006_order_user_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderlineitem",
            name="product_size",
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
