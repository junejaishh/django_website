# Generated by Django 3.1 on 2020-08-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_order_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]