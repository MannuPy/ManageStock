

from django.db import models

class Article(models.Model):
    IDART = models.AutoField(primary_key=True)
    RefArt = models.CharField(max_length=255)
    Designation = models.CharField(max_length=255)
    TypeArt = models.CharField(max_length=255)
    LOT = models.CharField(max_length=255)
    Conditionnement = models.CharField(max_length=255)
    CATEGORIE = models.CharField(max_length=255)
    TauxTVA = models.DecimalField(max_digits=5, decimal_places=2)
    PUSansBIC = models.DecimalField(max_digits=10, decimal_places=2)
    REMISE = models.DecimalField(max_digits=5, decimal_places=2)
    STOCKMIN = models.PositiveIntegerField()
    QTEENTREE = models.PositiveIntegerField()
    QTESORTIE = models.PositiveIntegerField()
    PumACHAT = models.DecimalField(max_digits=10, decimal_places=2)
    PumVENTE = models.DecimalField(max_digits=10, decimal_places=2)
    QTESTOCK = models.PositiveIntegerField()
    TOTALSTOCK = models.DecimalField(max_digits=10, decimal_places=2)
    ETATSTOCK = models.CharField(max_length=255)
    DatePremption = models.DateField()
    TEXT = models.TextField()

    def __str__(self):
        return self.RefArt  # Vous pouvez choisir un champ d'affichage par défaut ici
