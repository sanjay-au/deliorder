# Generated by Django 5.0.4 on 2024-04-12 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='fooditem',
            new_name='food_item',
        ),
    ]
