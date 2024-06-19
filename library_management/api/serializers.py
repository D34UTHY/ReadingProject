from rest_framework import serializers
from .models import Autor, Categoria, Livro

class SerializadorAutor(serializers.ModelSerializer):
    class Meta:
        modelo = Autor
        fields = '__all__'

class SerializadorCategoria(serializers.ModelSerializer):
    class Meta:
        modelo = Categoria
        fields = '__all__'

class SerializadorLivro(serializers.ModelSerializer):
        autor = SerializadorAutor()
        categoria = SerializadorCategoria()

        class Meta:
            modelo = Livro
            fields = '__all__'