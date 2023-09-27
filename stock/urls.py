from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Crée un routeur pour enregistrer les viewsets.
router = DefaultRouter()
router.register(r'articlecategories', views.articleCategoryViewSet)
router.register(r'articles', views.articleViewSet)
router.register(r'clientcategories', views.ClientCategoryViewSet)
router.register(r'villes', views.VilleViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'proformas', views.ProformaViewSet)
router.register(r'pro_articles', views.Pro_articleViewSet)
router.register(r'bc_articles', views.BC_articleViewSet)
router.register(r'bl_articles', views.BL_articleViewSet)
router.register(r'bonlivraisons', views.BonLivraisonViewSet)
router.register(r'factures', views.FactureViewSet)
router.register(r'bl_facts', views.BL_FactViewSet)
router.register(r'fournisseurs', views.FournisseurViewSet)
router.register(r'boncommandes', views.BonCommandeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
