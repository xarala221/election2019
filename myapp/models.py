from django.db import models



class ListeElecteur(models.Model):
  nom = models.CharField(max_length=120, null=True)
  prenom = models.CharField(max_length=120, null=True)
  numero_electeur = models.CharField(max_length=120, null=True)
  numero_identite  = models.CharField(max_length=120, null=True)

  def __str__(self):
    return self.nom


class MonElecteur(models.Model):
  nom = models.CharField(max_length=120, null=True)
  prenom = models.CharField(max_length=120, null=True)
  numero_electeur = models.CharField(max_length=120, null=True, unique=True)
  numero_identite  = models.CharField(max_length=120, null=True)
  region = models.CharField(max_length=120, null=True)

  def __str__(self):
    return self.nom
