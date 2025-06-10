from django.db import models

# Create your models here.

class Poruka(models.Model):
    tekst = models.CharField(max_length=255)

    def __str__(self):
        return self.tekst
