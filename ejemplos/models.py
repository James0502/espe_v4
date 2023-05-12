from django.contrib.auth.models import Group, User #importa los modelos Group y user
from django.db import models #importa los metodos necesarios para trabajar con modellos

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100, null=True, blank=True, verbose_name='Nombre habilidad')
    nivel = models.IntegerField(null=True, blank=True, verbose_name='Nivel Poder')
    estado = models.CharField(max_length=100, null=True, blank=True, default='Activo', verbose_name='Estado')   
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creación')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Actualización')
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades'
        ordering = ['nombre']   
    def __str__(self):
        return self.name

class Heroe(models.Model):
    habilidad = models.ForeignKey(Habilidad, on_delete=models.CASCADE)
    nombe_heroe = models.CharField(max_length=100, null=True, blank=True)
    nacionalidad_heroe = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True, default='Activo')   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = 'Heroe'
        verbose_name_plural = 'Heroes'
        ordering = ['nombe_heroe']
    
    def __str__(self):
        return self.nombe_heroe

def custom_upload_to(instance, filename):
    return 'product/' + filename

class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.IntegerField(null=True, blank=True)
    product_image = models.CharField(max_length=240, null=True, blank=True)
    product_state = models.CharField(max_length=100, null=True, blank=True, default='No')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']
    
    def __str__(self):
        return self.product_name
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    talla = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre

class proveedor(models.Model):
    descripcion=models.CharField(
        max_length=100,
        unique=True
    )

    direccion=models.CharField(
        max_length=250,
        null=True,blank=True
    )

    contacto=models.CharField(
        max_length=100
    )
    telefono=models.CharField(
        max_length=100,
        null=True, blank=True
    )
    email=models.CharField(
        max_length=250
    )
    def __str__(self):
            return'{}'.format(self.descripcion)
    
    def save(self):
        self.descripcion= self.descripcion.upper()
        super(proveedor, self).save()
    
    class Meta:
        verbose_name_plural= "Proveedores"




