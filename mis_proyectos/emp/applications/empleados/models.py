from django.db import models # type: ignore
from applications.departamentos.models import Departamento
from ckeditor.fields import RichTextField # type: ignore
# Create your models here.

class Habilidades(models.Model):

    habilidad = models.CharField('Habilidad', max_length = 50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):

    JOB_CHOICES = (
        ('0', 'matemático'),
        ('1', 'físico'),
        ('2', 'biólogo'),
        ('3', 'químico'),
        ('4', 'otro'),
    )

    first_name = models.CharField('Nombres', max_length = 60)
    last_name = models.CharField('Apellidos', max_length = 60)
    full_name = models.CharField('Nombres completos', 
                                 max_length=120, 
                                 blank=True)
    job = models.CharField('Trabajo', max_length = 1, choices = JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank = True, null = True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
    