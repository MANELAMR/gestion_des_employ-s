from django.db import models
import os
 

# Create your models here.

    

class Administrateur(models.Model):
   nom = models.CharField(max_length=50)
   prenom = models.CharField(max_length=50)
   adresse = models.CharField(max_length=100)
   email = models.EmailField()
   mot_de_passe = models.IntegerField()
      
