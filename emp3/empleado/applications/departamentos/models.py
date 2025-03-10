from django.db import models # type: ignore

class Departamento(models.Model):
   name = models.CharField("Nombre", max_length=50)
   short_name = models.CharField("Nombre Corto", max_length=20)
   anulate = models.BooleanField("Anulado", default=False)

   class Meta:
      verbose_name = "mi depa"
      verbose_name_plural = "mis depas"
      ordering = ['-name']
      unique_together = ['name', 'short_name']



   def __str__(self):
      return str(self.id) + "-" + self.name + "-" + self.short_name
   