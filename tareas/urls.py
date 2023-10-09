from django.urls import include, path

from rest_framework import routers
from tareas import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet, basename='usuarios')
router.register(r'proyectos', views.ProyectoViewSet, basename='proyectos')
router.register(r'tareas', views.TareaViewSet, basename='tareas')
urlpatterns = [
    path("api/v1/", include(router.urls)),
]
