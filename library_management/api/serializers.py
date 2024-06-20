from rest_framework import serializers
from .models import Autor, Categoria, Livro

# Criação dos serializadores para cada modelo
# Ele converterá os dados de cada modelo em um formato que poderá ser facilmente transformado em JSON
# para respostas de API e validado para entradas de API

class SerializadorAutor(serializers.ModelSerializer):
    class Meta:
        modelo = Autor # Indica qual modelo o serializador está associado
        fields = '__all__' # Inclui todos os campos do modelo no serializador

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