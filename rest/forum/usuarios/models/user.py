from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.db import models

class User(AbstractBaseUser):
    perfil = models.ForeignKey(Perfil, on_delete=models.PROTECT, related_name='users', verbose_name='Perfil')
    username = models.CharField(max_length=130, unique=True, verbose_name='Nome de Usuário', null=False)
    password = models.CharField(max_length=255, verbose_name='Senha', null=False)
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Data e hora de criação')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self): return self.username

    @property
    def name(self): return self.person.name if self.person else self.username