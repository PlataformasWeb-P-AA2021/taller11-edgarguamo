from django.db import models
from django.db.models.deletion import CASCADE

class Edificio(models.Model):
    nombre = models.CharField('Nombre del Propietario', max_length=30)
    direccion = models.CharField('Dirección del Edificio', max_length=50)
    ciudad = models.CharField(max_length=50)
    tipo = models.CharField(max_length=15)
    
    def __str__(self):
        return "%s, %s, %s, %s \n" % (self.nombre, self.direccion, self.ciudad, self.tipo)

class Departamento(models.Model):
    nombre = models.CharField('Nombre del Propietario', max_length=50)
    costo_dept = models.IntegerField('Costo del Departamento')
    num_cuartos = models.IntegerField('Número Cuartos')
    edificio = models.ForeignKey(Edificio, related_name='ubicacion',
     on_delete=CASCADE)

    def __str__(self):
        return "%s, %s, %s, %s" % (self.nombre, self.costo_dept, self.num_cuartos, self.edificio)

    