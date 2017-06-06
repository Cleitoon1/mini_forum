from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token

import rest.forum.posts.views as views

urlpatterns = {
    url(r'^topicos/$', views.TopicoView.as_view(), name="create"),
    url(r'^posts/$', views.PostView.as_view(), name="create"),
    url(r'^respostas/$', views.RespostaView.as_view(), name="create")
}

urlpatterns = format_suffix_patterns(urlpatterns)