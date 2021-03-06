# Generated by Django 3.1.7 on 2021-02-20 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoffeeMachine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('product_type', models.CharField(choices=[(1, 'COFFEE_MACHINE_LARGE'), (0, 'COFFEE_MACHINE_SMALL'), (2, 'ESPRESSO_MACHINE')], max_length=30)),
                ('model', models.CharField(choices=[(1, 'base model'), (2, 'premium model'), (3, 'deluxe model')], max_length=30)),
            ],
        ),
    ]
