
from django.db import models
from django.utils import timezone

class articleCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class article(models.Model):
    reference = models.CharField(max_length=255, unique=True)
    designation = models.CharField(max_length=255, unique=True)
    type_article = models.CharField(max_length=255)
    lot = models.CharField(max_length=255)
    packaging = models.CharField(max_length=255)
    category = models.ForeignKey(articleCategory, on_delete=models.CASCADE)
    remise = models.IntegerField()
    quantity_in = models.IntegerField()
    quantity_out = models.IntegerField()
    one_sell_price = models.IntegerField()
    total_stock = models.IntegerField()
    state_stock = models.SmallIntegerField()
    DatePremption = models.DateField(default=timezone.now)

    def __str__(self):
        return self.reference

class ClientCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Ville(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Client(models.Model):
    nom = models.CharField(max_length=255)
    category = models.ForeignKey(ClientCategory, on_delete=models.CASCADE)
    ifu = models.CharField(max_length=255, unique=True)
    rccm = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nom

class Proforma(models.Model):
    num_proforma = models.AutoField(primary_key=True)
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    date_proforma = models.DateTimeField()
    total_ht = models.IntegerField()
    total_bic = models.IntegerField()
    frais_livraison = models.IntegerField()
    total_tva = models.IntegerField()
    total_ttc = models.IntegerField()
    remise = models.IntegerField()
    net_a_payer = models.IntegerField()

    def __str__(self):
        return str(self.num_proforma)

class Pro_article(models.Model):
    proforma = models.ForeignKey(Proforma, on_delete=models.CASCADE)
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

    def __str__(self):
        return f"Proforma: {self.proforma.num_proforma}, article: {self.article.reference}"

class BC_article(models.Model):
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_one = models.IntegerField()

    def __str__(self):
        return f"article: {self.article.reference}, Quantity: {self.quantity}"

class BL_article(models.Model):
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price_one = models.IntegerField()

    def __str__(self):
        return f"article: {self.article.reference}, Quantity: {self.quantity}"

class BonLivraison(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    create_at = models.DateTimeField()
    mode_bl = models.CharField(max_length=255)
    total_ht = models.IntegerField()
    frais_transport = models.IntegerField()
    blArticles = models.ManyToManyField(BL_article)

    def __str__(self):
        return f"Client: {self.client.nom}, Date: {self.create_at}"

class Facture(models.Model):
    num_facture = models.IntegerField(unique=True)
    create_at = models.DateTimeField()
    nature_facture = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    total_ht = models.IntegerField()
    total_bic = models.IntegerField()
    frais_transport = models.IntegerField()
    remise = models.IntegerField()
    total_remise = models.IntegerField()
    total_ttc = models.IntegerField()
    net_a_payer = models.IntegerField()
    etat_fact = models.BooleanField()  # Nouvelle variable

    def __str__(self):
        return f"Numéro Facture: {self.num_facture}, Client: {self.client.nom}"

class BL_Fact(models.Model):
    bon_livraison = models.ForeignKey(BonLivraison, on_delete=models.CASCADE)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)

    def __str__(self):
        return f"Bon Livraison: {self.bon_livraison.num_bl}, Facture: {self.facture.num_facture}"

class Fournisseur(models.Model):
    nom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, unique=True)  # Téléphone est obligatoire
    address = models.TextField()
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    fax = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    ifu = models.CharField(unique=True, max_length=255)
    rccm = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.nom

class Vente(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    date_vente = models.DateTimeField()
    quantity = models.IntegerField()
    unit_price = models.IntegerField()

    def __str__(self):
        return f"Vente de {self.article.reference} à {self.client.nom}"

class StatClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    article = models.ForeignKey(article, on_delete=models.CASCADE)
    periode = models.CharField(max_length=255)  # Vous pouvez personnaliser la période
    vente_quantity = models.IntegerField()

    def __str__(self):
        return f"Statistique de {self.client.nom} pour {self.article.reference} en {self.periode}"



class BonCommande(models.Model):
    fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE)
    create_at = models.DateTimeField()
    ref_piece = models.CharField(max_length=255)
    frais_transport = models.IntegerField()
    bcarticles = models.ManyToManyField(BC_article)
    total_bic = models.IntegerField()
    total_ht = models.IntegerField()
    total_tva = models.IntegerField()
    remise = models.IntegerField()
    total_ttc = models.IntegerField()
    total_remise = models.IntegerField()
    net_a_payer = models.IntegerField()

    def __str__(self):
        return f"Référence: {self.ref_piece}, Fournisseur: {self.fournisseur.nom}"
