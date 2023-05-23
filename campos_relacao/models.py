from django.db import models

# Create your models here.

from django.db import models

# classe abstrata
class Pessoa(models.Model):
    nome = models.CharField(max_length=100, default=None)
    
    class Meta:
        abstract = True

class Escritor(Pessoa):
    pseudonimo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nome}, denominado '{self.pseudonimo}'"

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    ecritor = models.ForeignKey(Escritor, on_delete=models.CASCADE, related_name='livros')
    def __str__(self):
        return self.titulo
    

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    alunos = models.ManyToManyField(Aluno, related_name="disciplinas")
    def __str__(self):
        return self.nome



class Familia(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    
class Morada(models.Model):
    rua = models.CharField(max_length=100)
    localidade = models.CharField(max_length=100)
    familia = models.OneToOneField(Familia, on_delete=models.CASCADE, related_name="morada")

    def __str__(self):
        return f'{self.familia}: {self.localidade}'
    