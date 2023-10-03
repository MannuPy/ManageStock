from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated  # Importez le décorateur d'autorisation IsAuthenticated
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
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated] 

class articleViewSet(viewsets.ModelViewSet):
    queryset = article.objects.all()
    serializer_class = articleSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated] 

class ClientCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClientCategory.objects.all()
    serializer_class = ClientCategorySerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated] 

class VilleViewSet(viewsets.ModelViewSet):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class ProformaViewSet(viewsets.ModelViewSet):
    queryset = Proforma.objects.all()
    serializer_class = ProformaSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class Pro_articleViewSet(viewsets.ModelViewSet):
    queryset = Pro_article.objects.all()
    serializer_class = Pro_articleSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class BC_articleViewSet(viewsets.ModelViewSet):
    queryset = BC_article.objects.all()
    serializer_class = BC_articleSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class BL_articleViewSet(viewsets.ModelViewSet):
    queryset = BL_article.objects.all()
    serializer_class = BL_articleSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class BonLivraisonViewSet(viewsets.ModelViewSet):
    queryset = BonLivraison.objects.all()
    serializer_class = BonLivraisonSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class BL_FactViewSet(viewsets.ModelViewSet):
    queryset = BL_Fact.objects.all()
    serializer_class = BL_FactSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class FournisseurViewSet(viewsets.ModelViewSet):
    queryset = Fournisseur.objects.all()
    serializer_class = FournisseurSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout

class BonCommandeViewSet(viewsets.ModelViewSet):
    queryset = BonCommande.objects.all()
    serializer_class = BonCommandeSerializer
    authentication_classes = [SessionAuthentication]  # Ajoutez l'authentification ici
    permission_classes = [IsAuthenticated]  # Ajout