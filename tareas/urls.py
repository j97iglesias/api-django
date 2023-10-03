from django.urls import include, path

from rest_framework import routers
from tareas import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path("api/v1/", include(router.urls)),
]
