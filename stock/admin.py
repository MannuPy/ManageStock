# stock/admin.py

from django.contrib import admin
from .models import articleCategory, article, ClientCategory, Ville, Client, Proforma, Pro_article, BC_article, BL_article, BonLivraison, Facture, BL_Fact, Fournisseur, BonCommande

# Enregistrez tous les modèles dans l'interface d'administration
admin.site.register(articleCategory)
admin.site.register(article)
admin.site.register(ClientCategory)
admin.site.register(Ville)
admin.site.register(Client)
admin.site.register(Proforma)
admin.site.register(Pro_article)
admin.site.register(BC_article)
admin.site.register(BL_article)
admin.site.register(BonLivraison)
admin.site.register(Facture)
admin.site.register(BL_Fact)
admin.site.register(Fournisseur)
admin.site.register(BonCommande)
