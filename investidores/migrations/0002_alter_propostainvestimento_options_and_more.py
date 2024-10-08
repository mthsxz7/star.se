# Generated by Django 5.1 on 2024-08-11 23:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresarios', '0007_delete_propostainvestimento'),
        ('investidores', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propostainvestimento',
            options={},
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='propostas_investidores', to='empresarios.empresas'),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='investidor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='propostas_investidores', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='percentual',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='rg',
            field=models.FileField(blank=True, null=True, upload_to='rg'),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='selfie',
            field=models.FileField(blank=True, null=True, upload_to='selfie'),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='status',
            field=models.CharField(choices=[('AS', 'Aguardando assinatura'), ('PE', 'Proposta enviada'), ('PA', 'Proposta aceita'), ('PR', 'Proposta recusada')], default='AS', max_length=2),
        ),
        migrations.AlterField(
            model_name='propostainvestimento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
