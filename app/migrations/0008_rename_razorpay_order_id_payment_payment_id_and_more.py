# Generated by Django 5.1.3 on 2024-12-10 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_order_id',
            new_name='payment_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_id',
            new_name='payment_order_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_status',
            new_name='payment_status',
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='division',
            field=models.CharField(choices=[('Dhaka', 'Dhaka'), ('Chattogram', 'Chattogram'), ('Rajshahi', 'Rajshahi'), ('Khulna', 'Khulna'), ('Barishal', 'Barishal'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Mymensingh', 'Mymensingh')], max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.payment'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]