from django.db import models

# Criação dos modelos Autor, Categoria e Livro

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000)

    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(max_length=2000)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    dataPublicacao = models.DateField()

    def __str__(self):
        return self.title