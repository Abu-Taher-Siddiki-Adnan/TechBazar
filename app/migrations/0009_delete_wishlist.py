# Generated by Django 5.1.3 on 2024-12-10 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_razorpay_order_id_payment_payment_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
