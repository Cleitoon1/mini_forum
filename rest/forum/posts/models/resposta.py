from datetime import datetime

from django.forms import models

from rest.forum.posts.models.post import Post
from rest.forum.usuarios.models.user import User


class Resposta(models.Model):
    texto = models.CharField(max_length=500, null=False)
    data_criacao = models.DateField(default=datetime.now())
    autor = models.OneToOneField(User, null=False)
    post = models.ForeignKey(Post, related_name='post')

    class Meta:
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'

    def __str__(self):
        return "Autor: " + self.autor + " Resposta: " + self.texto