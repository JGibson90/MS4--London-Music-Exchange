# Generated by Django 3.2 on 2022-01-14 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="blog_date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
