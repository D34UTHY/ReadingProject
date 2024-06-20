from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from .models import Autor, Categoria, Livro
from .serializers import SerializadorAutor, SerializadorCategoria, SerializadorLivro

class ViewSetLivro(viewsets.ModelViewSet):
    # Define o queryset padrão para o viewset atual
    queryset = Livro.objects.all()
    # Define o serializer a ser usado para o viewset atual
    serializer_class = SerializadorLivro
    # Define as permissões necessárias para acessar a viewset
    permission_classes = [IsAuthenticated]

    # Sobrescreve o método retrieve para tratar o caso de Livro não encontrado
    def retrieve(self, request, *args, **kwargs):
        try:
            # Chama o método retrieve do ModelViewSet
            return super().retrieve(request, *args, **kwargs)
        except Livro.DoesNotExist:
            # Lança uma excessão caso o livro não seja encontrado
            raise NotFound(detail="Livro não encontrado!")
        
    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Livro.DoesNotExist:
            raise NotFound(detail="Livro não encontrado!")
        
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Livro.DoesNotExist:
            raise NotFound(detail="Livro não encontrado!")
        

class ViewSetAutor(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = SerializadorAutor
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Autor.DoesNotExist:
            raise NotFound(detail="Autor não encontrado!")
        
    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Autor.DoesNotExist:
            raise NotFound(detail="Autor não encontrado!")
        
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Autor.DoesNotExist:
            raise NotFound(detail="Autor não encontrado!")

class ViewSetCategoria(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = SerializadorAutor
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        try:
            return super().retrieve(request, *args, **kwargs)
        except Categoria.DoesNotExist:
            raise NotFound(detail="Categoria não encontrada!")
        
    def update(self, request, *args, **kwargs):
        try:
            return super().update(request, *args, **kwargs)
        except Categoria.DoesNotExist:
            raise NotFound(detail="Categoria não encontrada!")
        
    def destroy(self, request, *args, **kwargs):
        try:
            return super().destroy(request, *args, **kwargs)
        except Categoria.DoesNotExist:
            raise NotFound(detail="Categoria não encontrada!")