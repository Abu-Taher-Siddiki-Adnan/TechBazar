# Generated by Django 5.1.3 on 2024-12-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_wishlist_unique_together_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_order_id',
            new_name='transaction_id',
        ),
        migrations.AddField(
            model_name='payment',
            name='currency',
            field=models.CharField(default='BDT', max_length=10),
        ),
    ]
