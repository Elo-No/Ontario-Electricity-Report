# Generated by Django 4.1.3 on 2022-11-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DemandReport",
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
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "modified",
                    models.DateTimeField(auto_now=True, verbose_name="Modified at"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Is deleted ?"),
                ),
                (
                    "is_archived",
                    models.BooleanField(default=False, verbose_name="Is archived ?"),
                ),
                ("date", models.DateTimeField(verbose_name="Date")),
                ("hour", models.PositiveIntegerField(verbose_name="Hour")),
                (
                    "market_demand",
                    models.PositiveIntegerField(verbose_name="Market Demand"),
                ),
                (
                    "ontario_demand",
                    models.PositiveIntegerField(verbose_name="Ontario Demand"),
                ),
                (
                    "market_peak_day",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Market Peak Day"
                    ),
                ),
                (
                    "Ontario_peak_day",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Ontario Peak Day"
                    ),
                ),
                (
                    "market_peak_month",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Market Peak Month"
                    ),
                ),
                (
                    "ontario_peak_month",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="Ontario Peak Month"
                    ),
                ),
            ],
            options={
                "unique_together": {("date", "hour")},
            },
        ),
    ]
