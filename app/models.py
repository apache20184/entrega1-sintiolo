from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre=models.CharField(max_length=30)
    fecha_de_nacimiento=models.DateField()
    edad=models.IntegerField()
    def __str__(self):
        return f'soy un familiar llamado {self.nombre}'
    
 