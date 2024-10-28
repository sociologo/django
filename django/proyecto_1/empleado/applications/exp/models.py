from django.db import models # type: ignore

# Create your models here.
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self) -> str:
        return self.titulo + " " + self.subtitulo
    