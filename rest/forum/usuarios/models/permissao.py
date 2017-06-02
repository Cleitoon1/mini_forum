from django.db import models


class Permissao(models.Model):
    nome = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Permissão'
        verbose_name_plural = 'Permissões'

    def __str__(self):
        return "Id: " + self.id + " Tipo: " + self.nome