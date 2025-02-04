# Generated by Django 5.0.4 on 2024-04-13 09:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_quantity'),
        ('food', '0002_fooditems_stock_alter_custom_user_phone'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, default=1, max_digits=3)),
                ('address', models.TextField(default='')),
                ('phone', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(choices=[('pending', 'Pending'), ('picked', 'Order Picked'), ('delivery', 'Out For Delivery'), ('delivered', 'Delivered')], max_length=20)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.fooditems')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
