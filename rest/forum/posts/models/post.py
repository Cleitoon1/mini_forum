import datetime
from django.forms import models

from rest.forum.posts.models.topico import Topico
from rest.forum.usuarios.models.user import User


class Post(models.Model):
    titulo = models.CharField(max_length=200, null=False, verbose_name='Título')
    texto = models.CharField(max_length=500, null=False, verbose_name='Texto')
    data_criacao = models.DateField(default=datetime.now(), auto_now_add=True, verbose_name='Data e hora de criação')
    autor = models.OneToOneField(User, verbose_name='Autor', null=False)
    topico = models.ForeignKey(Topico, related_name='topicos')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return "Título: " + self.titulo + " Data de Criação: " + self.data_criacao + " Data de publicação: " + self.data_publicacao + " Texto: " + self.texto
