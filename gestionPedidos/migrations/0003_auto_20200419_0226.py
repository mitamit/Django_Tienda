# Generated by Django 3.0.5 on 2020-04-19 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0002_auto_20200414_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
