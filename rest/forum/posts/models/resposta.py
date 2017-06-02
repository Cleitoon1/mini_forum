from datetime import datetime

from django.forms import models

from forum.posts.models.post import Post


class Resposta(models.Model):
    texto = models.CharField(max_length=500, null=False)
    data_criacao = models.DateField(default=datetime.now())
    autor = models.OneToOneField(Perfil, null=False)
    post = models.ForeignKey(Post, related_name='post')

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return "Autor: " + self.autor + " Resposta: " + self.texto