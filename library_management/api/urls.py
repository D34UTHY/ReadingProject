from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ViewSetAutor, ViewSetCategoria, ViewSetLivro

# Cria um roteador padrão do Django REST Framework
router = DefaultRouter()

# Registra as rotas para os viewsets de Livro, Autor e Categoria.
router.register(r'livros', ViewSetLivro)
router.register(r'autores', ViewSetAutor)
router.register(r'categorias', ViewSetCategoria)

# Define as URLs da aplicação, nesse caso, todas geradas pelo roteador que
# automaticamente cria as rotas padrão para métodos CRUD (criar, ler, atualizar, deletar)
urlpatterns = [
    path('', include(router.urls))
]