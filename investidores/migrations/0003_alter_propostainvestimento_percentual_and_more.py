# Generated by Django 5.1 on 2024-08-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investidores', '0002_alter_propostainvestimento_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propostainvestimento',
            name='percentual',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='valor',
            field=models.FloatField(),
        ),
    ]
