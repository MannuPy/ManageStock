from rest_framework import serializers
from .models import articleCategory, article, ClientCategory, Ville, Client, Proforma, Pro_article, BC_article, BL_article, BonLivraison, Facture, BL_Fact, Fournisseur, BonCommande

class articleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = articleCategory
        fields = '__all__'

class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = article
        fields = '__all__'

class ClientCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientCategory
        fields = '__all__'

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ProformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proforma
        fields = '__all__'

class Pro_articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro_article
        fields = '__all__'

class BC_articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BC_article
        fields = '__all__'

class BL_articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BL_article
        fields = '__all__'

class BonLivraisonSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonLivraison
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'

class BL_FactSerializer(serializers.ModelSerializer):
    class Meta:
        model = BL_Fact
        fields = '__all__'

class FournisseurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fournisseur
        fields = '__all__'

class BonCommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BonCommande
        fields = '__all__'
