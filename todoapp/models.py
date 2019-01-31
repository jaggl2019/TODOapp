from django.db import models

# Create your models here.
class TodoTBL(models.Model):
    accion = models.CharField(max_length=40)
    estado = models.BooleanField(default=False)
    def __str__(self):
        return self.accion