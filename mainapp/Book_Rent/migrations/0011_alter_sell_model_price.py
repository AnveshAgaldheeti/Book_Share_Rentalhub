# Generated by Django 5.0.3 on 2024-05-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Rent', '0010_alter_sell_model_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sell_model',
            name='price',
            field=models.IntegerField(),
        ),
    ]
