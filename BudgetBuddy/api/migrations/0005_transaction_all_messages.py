# Generated by Django 4.2.9 on 2024-02-03 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_transaction_username_alter_transaction_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="all_messages",
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
