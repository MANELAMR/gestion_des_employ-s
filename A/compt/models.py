from django.db import models


# Create your models here.


   


class Employer(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    dateN = models.DateField(null=True)
    nbr_femmes = models.IntegerField()
    num_inférentiek_inf = models.IntegerField()
    situation_familiale = models.CharField(max_length=50)
    categorie = models.IntegerField()
    rang = models.IntegerField()
    nbr_enfants = models.IntegerField()
    num_telephon = models.CharField(max_length=16)
    email = models.EmailField()
    sex= models.CharField(max_length=10,choices=[('H','Homme'),('F','Femme')])
    Nommarital = models.CharField(max_length=50)
    Date_de_recrutement=models.DateField(null=True)
    postes=models.CharField(max_length=500)
    


class Administrateur(models.Model):
    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)
    phone_number= models.CharField(max_length=16)
    email = models.EmailField()
    sex= models.CharField(max_length=10)
    mot_passe =models.CharField(max_length=10)
    photo=models.ImageField()
   