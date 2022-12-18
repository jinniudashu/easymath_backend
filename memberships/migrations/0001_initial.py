# Generated by Django 4.1.3 on 2022-12-18 01:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Membership",
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
                ("slug", models.SlugField()),
                (
                    "membership_type",
                    models.CharField(
                        choices=[
                            ("Annual", "年度会员"),
                            ("Semi-annual", "半年会员"),
                            ("Monthly", "月会员"),
                            ("Free", "free"),
                        ],
                        default="Free",
                        max_length=30,
                        verbose_name="会员类型",
                    ),
                ),
                ("price", models.IntegerField(default=15, verbose_name="价格")),
                (
                    "stripe_plan_id",
                    models.CharField(max_length=40, verbose_name="Stripe Plan ID"),
                ),
            ],
            options={"verbose_name": "会员类型", "verbose_name_plural": "会员类型",},
        ),
        migrations.CreateModel(
            name="UserMembership",
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
                    "stripe_customer_id",
                    models.CharField(max_length=40, verbose_name="Stripe Customer ID"),
                ),
                (
                    "membership",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="memberships.membership",
                        verbose_name="会员类型",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="用户",
                    ),
                ),
            ],
            options={"verbose_name": "会员用户", "verbose_name_plural": "会员用户",},
        ),
        migrations.CreateModel(
            name="Subscription",
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
                    "stripe_subscription_id",
                    models.CharField(
                        max_length=40, verbose_name="Stripe Subscription ID"
                    ),
                ),
                ("active", models.BooleanField(default=True, verbose_name="有效期内")),
                (
                    "user_membership",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="memberships.usermembership",
                        verbose_name="会员用户",
                    ),
                ),
            ],
            options={"verbose_name": "订阅记录", "verbose_name_plural": "订阅记录",},
        ),
    ]
