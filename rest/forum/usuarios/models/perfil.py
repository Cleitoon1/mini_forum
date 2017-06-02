from django.db import models

from forum.usuarios.models.permissao import Permissao


class Perfil(models.Model):
    nome = models.CharField(max_length=130, verbose_name='Nome')
    bio = models.CharField(max_length=255, verbose_name='Bio')
    permissoes = models.ManyToManyField(Permissao, related_name='profiles', verbose_name='Permissões')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'

    def __str__(self):
        return '%s (%d permissões)' % (
        self.name, self.permissions.count()) if self.permissions else '%s (sem permissões)' % self.name

    def has_perm(self, permission):
        return permission.id in [perm.id for perm in self.permissions.all()]