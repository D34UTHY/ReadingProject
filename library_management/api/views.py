from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Autor, Categoria, Livro
from .serializers import SerializadorAutor, SerializadorCategoria, SerializadorLivro

class ViewSetLivro(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = SerializadorLivro
    permission_classes = [IsAuthenticated]

class ViewSetAutor(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = SerializadorAutor
    permission_classes = [IsAuthenticated]

class ViewSetCategoria(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = SerializadorAutor
    permission_classes = [IsAuthenticated]