# Generated by Django 5.0.3 on 2024-05-02 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book_Rent', '0008_sell_model_cat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sell_model',
            old_name='cat',
            new_name='categories',
        ),
    ]
