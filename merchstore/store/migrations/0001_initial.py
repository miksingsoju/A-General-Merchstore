# Generated by Django 5.1.6 on 2025-04-16 08:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=99)),
                ('stock', models.PositiveBigIntegerField(default=0)),
                ('status', models.CharField(choices=[('available', 'Available'), ('on_sale', 'On sale'), ('out_of_stock', 'Out of stock')], default='available', max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.profile')),
                ('productType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.producttype')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('on cart', 'ON CART'), ('to pay', 'TO PAY'), ('to ship', 'TO SHIP'), ('to receive', 'TO RECEIVE'), ('delivered', 'DELIVERED')], max_length=20)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user_management.profile')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product')),
            ],
        ),
    ]
