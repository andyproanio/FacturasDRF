from rest_framework import routers
from django.urls import path

from .api import *
from .views import FiltrarInventario

router = routers.DefaultRouter()
router.register(r'api/SubirComprobantes', SubirComprobantesViewSet, 'SubirArchivo')

urlpatterns = [
    path('api/Inventario', InventarioViewSet.as_view({'get': 'list'})),
    path('api/FiltrarInventario', FiltrarInventario.as_view()),
]

urlpatterns += router.urls
