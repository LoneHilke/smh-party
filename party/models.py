from django.db import models

# Create your models here.
class Fest(models.Model):
  name = models.CharField(max_length=100)
  kontakt = models.CharField(max_length=100)
  fest = models.CharField(max_length=100)
  dato = models.DateField()
  tid = models.CharField(max_length=100)
  playlist = models.CharField(max_length=100)
  adresse = models.CharField(max_length=100)
  optrædende = models.CharField(max_length=100, blank=True)
  telt = models.BooleanField(default=True)
  oplysninger = models.TextField(blank=True)

  def __str__(self):
    return self.name

class Mig(models.Model):
  årstal = models.CharField(max_length=100)
  info = models.TextField(blank=True)

class Anmeld(models.Model):
  created_on = models.DateTimeField(auto_now_add=True)
  anmeld = models.TextField()
  navn = models.CharField (max_length=100)

  def __str__(self):
    return self.navn