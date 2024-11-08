from django.db import models # type: ignore

# Create your models here.

class Departamento(models.Model):
    # name = models.CharField('Nombre', max_length=50, editable=False)
    name = models.CharField('Nombre', max_length=50)
    short_name = models.CharField('Nombre corto', max_length=20, unique=True)
    anulate =models.BooleanField('Anulado', default=False)

    class Meta:
        verbose_name = 'Mi depart'
        verbose_name_plural = 'Departamentos de investigacion'
        ordering = ['-name']
        unique_together = ['name', 'short_name']

    def __str__(self):
        return str(self.id) + '-' + self.name  + '-' + self.short_name



