from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('usuario', views.UsuarioView)
router.register('escola', views.EscolaView)
router.register('cidade', views.CidadeView)

urlpatterns = [
    path('', include(router.urls)),
]