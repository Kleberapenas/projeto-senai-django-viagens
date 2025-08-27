from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='static/viagens/img/')
    data_viagem = models.DateField()

    def __str__(self):
        return self.titulo