from django.db import models

class Blog(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Conta(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='dono')
    github = models.URLField()
    pythonanywhere = models.URLField()


class Area(models.Model):
    nome = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="areas")

    def __str__(self):
        return self.nome


class Autor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Artigo(models.Model):

    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    area =  models.ForeignKey(Area, on_delete=models.CASCADE, related_name='artigos')
    autores = models.ManyToManyField(Autor, related_name='artigos')
    likes = models.IntegerField(default=0)

    def __str__(self):
        autores = []
        for autor in self.autores.all():
            autores.append(autor.nome)
        return f'{self.titulo} ({ ", ".join(autores) }) - {self.likes}⭐'
    

class Comentario(models.Model):
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.TextField()
    nome = models.CharField(max_length=50, default="", null= None)

    def __str__(self):
        return f'{self.texto[:20]+".."} ({ self.nome })'
