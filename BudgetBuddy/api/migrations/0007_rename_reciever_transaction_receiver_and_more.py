# Generated by Django 4.2.9 on 2024-02-03 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_transaction_all_messages"),
    ]

    operations = [
        migrations.RenameField(
            model_name="transaction", old_name="reciever", new_name="receiver",
        ),
        migrations.AddField(
            model_name="transaction",
            name="receiver_category",
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
