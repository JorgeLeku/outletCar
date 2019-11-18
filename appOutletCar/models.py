from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User


# Create your models here.
class Lugar(models.Model):
    cod_ciudad = models.CharField(null=False, primary_key=True, max_length=4)
    ciudad = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):

        return self.cod_ciudad


class Marca(models.Model):
    nombre_Marca = models.CharField(max_length=100, null=False, primary_key=True)
    descripcion = models.CharField(max_length=1000)
    fecha_creacion = models.DateField()

    def __str__(self):

        return self.nombre_Marca


class Modelo(models.Model):
    nombre_Modelo = models.CharField(max_length=100, null=False, primary_key=True)
    categoria = models.CharField(max_length=100)
    traccion = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):

        return self.nombre_Modelo


class Coche(models.Model):
    n_bastidor = models.CharField(max_length=100, null=False, primary_key=True)
    color = models.CharField(max_length=100)
    anyo = models.IntegerField()
    n_km = models.IntegerField()
    combustible = models.CharField(max_length=100)
    potencia = models.IntegerField()
    precio = models.FloatField()
    cambio = models.CharField(max_length=100)
    consumo = models.FloatField()
    comentario = models.CharField(max_length=1000)
    fotoCoche = models.ImageField(upload_to='images/', default='images/None/no-img.jpg')
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=200, unique=True, default='a')
    def __str__(self):
        return self.n_bastidor

    def body_preview(self):
        return self.body[:50]


class Usuario(models.Model):
    correo = models.CharField(max_length=100, null=False, primary_key=True)
    nombre_usuario = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.IntegerField()
    contrasenya = models.CharField(max_length=100)
    coche = models.ForeignKey(Coche, on_delete=models.CASCADE, null=True)

    def __str__(self):

        return self.correo


class Comment(models.Model):
    coche = models.ForeignKey(Coche,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)