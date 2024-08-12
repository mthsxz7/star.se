from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

from datetime import date

class Empresas(models.Model):
    tempo_existencia_choices = (
        ('-6', 'Menos de 6 meses'),
        ('+6', 'Mais de 6 meses'),
        ('+1', 'Mais de 1 ano'),
        ('+5', 'Mais de 5 anos'),
    )
    estagio_choices = (
        ('I', 'Tenho apenas uma ideia'),
        ('MVP', 'Possuo um MVP'),
        ('MVPP', 'Possuo um MVP com clientes pagantes'),
        ('E', 'Empresa pronta para escalar'),
    )
    area_choices = (
        ('ED', 'Ed-tech'),
        ('FT', 'Fintech'),
        ('AT', 'Agrotech'),
    )
    
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18)
    site = models.URLField(blank=True, null=True)
    tempo_existencia = models.CharField(max_length=2, choices=tempo_existencia_choices, default='-6')
    descricao = models.TextField()
    data_final_captacao = models.DateField()
    percentual_equity = models.DecimalField(max_digits=5, decimal_places=2)
    estagio = models.CharField(max_length=4, choices=estagio_choices, default='I')
    area = models.CharField(max_length=3, choices=area_choices)
    publico_alvo = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    pitch = models.FileField(upload_to='pitches/')
    logo = models.FileField(upload_to='logos/', blank=True, null=True)  # Substituído por CharField

    def __str__(self):
        username = getattr(self.user, 'username', 'Usuário Desconhecido')
        return f'{username} | {self.nome}'

    @property
    def status(self):
        if date.today() > self.data_final_captacao:
            return mark_safe('<span class="badge bg-success">Captação finalizada</span>')
        return mark_safe('<span class="badge bg-primary">Em captação</span>')

    @property
    def valuation(self):
        return f'{(100 * self.valor) / self.percentual_equity:.2f}'
    
class Documento(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    arquivo = models.FileField(upload_to="documentos")

    def __str__(self):
        return str(self.titulo) if self.titulo else "Título indisponível"

class Metricas(models.Model):
    empresa = models.ForeignKey(Empresas, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=30)
    valor = models.FloatField()

    def __str__(self):
        return str(self.titulo) if str(self.titulo) else "Título indisponível"

