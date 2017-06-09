from rest_framework import generics, permissions

#Permissões customizadas
class RestPermission(permissions.BasePermission):
    mensagem = "Você não tem autorização para acessar este recurso"

    def has_permission(self, request, view):
        # permission = models.Permission.objects.filter(action=view.action_type, view=view.view_name).first()
        # if permission and request.user.id:
        #     return request.user.profile.has_perm(permission)
        # return True
        pass


class GenericList(generics.ListAPIView):
    action_type = 'list'


class GenericRetrieve(generics.RetrieveAPIView):
    action_type = 'retrieve'


class GenericCreate(generics.CreateAPIView):
    action_type = 'create'


class GenericUpdate(generics.UpdateAPIView):
    action_type = 'update'


class GenericDelete(generics.DestroyAPIView):
    action_type = 'delete'