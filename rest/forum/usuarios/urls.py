from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

import rest.forum.usuarios.views as views

urlpatterns = {
    url(r'^permissoes/$', views.PermissaoView.as_view(), name="create"),
    url(r'^usuarios/$', views.UserView.as_view(), name="create")
}

urlpatterns = format_suffix_patterns(urlpatterns)