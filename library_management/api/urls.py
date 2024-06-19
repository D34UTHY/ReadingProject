from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSetAutor, ViewSetCategoria, ViewSetLivro

router = DefaultRouter()
router.register(r'livros', ViewSetLivro)
router.register(r'autores', ViewSetAutor)
router.register(r'categorias', ViewSetCategoria)

urlpatterns = [
    path('', include(router.urls))
]