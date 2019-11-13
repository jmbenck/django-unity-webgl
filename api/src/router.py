from usuarios.api.viewsets import UsuarioView, EscolaView, CidadeView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UsuarioView, base_name='usuario')
router.register('escola', EscolaView)
router.register('cidade', CidadeView)
