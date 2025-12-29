from django.db import models

class RolModel(models.Model):
    Rol = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return f"{self.Rol}"