# Generated by Django 5.0.4 on 2024-04-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_alter_order_order_status_alter_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Order Picked', 'Order Picked'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered')], max_length=20),
        ),
    ]
