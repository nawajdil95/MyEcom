# Generated by Django 4.0.1 on 2022-02-15 11:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm', '0002_product_delete_upload_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.IntegerField()),
                ('address', models.CharField(blank=True, default='', max_length=50)),
                ('phone', models.IntegerField()),
                ('date', models.DateField(default=datetime.datetime.today)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.register_info')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecomm.product')),
            ],
        ),
    ]
