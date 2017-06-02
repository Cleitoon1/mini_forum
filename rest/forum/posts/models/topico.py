from django.forms import models


class Topico(models.Model):
    nome = models.CharField(max_length=200, null=False, unique=True, verbose_name='Nome')

    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'

    def __str__(self):
        return 'Tópico: ' + self.nome


