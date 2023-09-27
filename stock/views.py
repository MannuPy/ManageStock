from rest_framework import viewsets
from .models import (
    articleCategory, article, ClientCategory, Ville, Client,
    Proforma, Pro_article, BC_article, BL_article,
    BonLivraison, Facture, BL_Fact,
    Fournisseur, BonCommande
)
from .serializers import (
    articleCategorySerializer, articleSerializer, ClientCategorySerializer,
    VilleSerializer, ClientSerializer, ProformaSerializer, Pro_articleSerializer,
    BC_articleSerializer, BL_articleSerializer, BonLivraisonSerializer,
    FactureSerializer, BL_FactSerializer, FournisseurSerializer, BonCommandeSerializer
)

class articleCategoryViewSet(viewsets.ModelViewSet):
    queryset = articleCategory.objects.all()
    serializer_class = articleCategorySerializer

class articleViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = articleSerializer

class ClientCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer

class VilleViewSet(viewsets.ModelViewSet):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProformaViewSet(viewsets.ModelViewSet):
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer

class Pro_articleViewSet(viewsets.ModelViewSet):
    queryset = Pro_article.objects.all()
    serializer_class = Pro_articleSerializer

class BC_articleViewSet(viewsets.ModelViewSet):
    queryset = BC_article.objects.all()
    serializer_class = BC_articleSerializer

class BL_articleViewSet(viewsets.ModelViewSet):
    queryset = BL_article.objects.all()
    serializer_class = BL_articleSerializer

class BonLivraisonViewSet(viewsets.ModelViewSet):
    queryset = BonLivraison.objects.all()
    serializer_class = BonLivraisonSerializer

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class BL_FactViewSet(viewsets.ModelViewSet):
    queryset = BL_Fact.objects.all()
    serializer_class = BL_FactSerializer

class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer

class BonCommandeViewSet(viewsets.ModelViewSet):
    queryset = BonCommande.objects.all()
    serializer_class = BonCommandeSerializer
