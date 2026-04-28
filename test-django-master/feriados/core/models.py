from django.db import models

class FeriadosModel(models.Model):
    nome = models.CharField('Feriado', max_length=250)
    dia = models.IntegerField('Data')
    mes = models.IntegerField('Mês')
    modificado = models.DateTimeField(verbose_name='modificado_em', auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.nome