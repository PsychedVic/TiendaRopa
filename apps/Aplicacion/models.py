from django.db import models

# Create your models here.

class TipoRopa(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Ropa(models.Model):
    TCHOICES = [
        ("S","S"),
        ("M","M"),
        ("L","L"),
    ]
    nombre_estilo = models.TextField()
    Tipo_ropa = models.ForeignKey(TipoRopa, on_delete = models.PROTECT)
    talla = models.CharField(max_length=1, choices=TCHOICES)
    color = models.TextField()
    precio = models.FloatField()
    # TODO: Define fields here

    class Meta:
        """Meta definition for Ropa."""

        verbose_name = 'Ropa'
        verbose_name_plural = 'Ropas'

    def __str__(self):
        """Unicode representation of Ropa."""
        return self.nombre_estilo + " Precio: " + str(self.precio)

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    nit = models.TextField(blank=True, default="C/F")
    direccion = models.TextField(blank=True, default="Ciudad")
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nombre + " " + self.apellido

class Factura(models.Model):
    PAYMENT_CHOICES = [
        ("efectivo", "efectivo"),
        ("tarjeta", "tarjeta"),
        ("ccuponu", "cupon"),
    ]
    numero_factura = models.CharField(max_length=12)
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    orden = models.OneToOneField("Orden", on_delete=models.CASCADE)
    pago = models.CharField(max_length=10, choices=PAYMENT_CHOICES)

    def __str__(self):
        return str(self.orden.id)

class Orden(models.Model):
    """Customer orders and state management."""

    # TODO: delivery_type: To eat here or carry out

    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ManyToManyField(Ropa, through="OrdenDetalle")
    total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

class OrdenDetalle(models.Model):
    """Order detail as quantity of each product and price."""

    orden = models.ForeignKey(Orden, on_delete=models.PROTECT)
    producto = models.ForeignKey(Ropa, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.producto.nombre_estilo

