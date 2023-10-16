"""
URL configuration for ManageStock project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
# Importez les viewsets de votre application stock
from stock.views import (
    articleCategoryViewSet,
    articleViewSet,
    ClientCategoryViewSet,
    VilleViewSet,
    ClientViewSet,
    ProformaViewSet,
    Pro_articleViewSet,
    BC_articleViewSet,
    BL_articleViewSet,
    BonLivraisonViewSet,
    FactureViewSet,
    BL_FactViewSet,
    FournisseurViewSet,
    BonCommandeViewSet,
)

# Créez un routeur pour les viewsets de votre application stock
from rest_framework.routers import DefaultRouter

stock_router = DefaultRouter()
stock_router.register(r'articlecategories', articleCategoryViewSet)
stock_router.register(r'articles', articleViewSet)
stock_router.register(r'clientcategories', ClientCategoryViewSet)
stock_router.register(r'villes', VilleViewSet)
stock_router.register(r'clients', ClientViewSet)
stock_router.register(r'proformas', ProformaViewSet)
stock_router.register(r'pro_articles', Pro_articleViewSet)
stock_router.register(r'bc_articles', BC_articleViewSet)
stock_router.register(r'bl_articles', BL_articleViewSet)
stock_router.register(r'bonlivraisons', BonLivraisonViewSet)
stock_router.register(r'factures', FactureViewSet)
stock_router.register(r'bl_facts', BL_FactViewSet)
stock_router.register(r'fournisseurs', FournisseurViewSet)
stock_router.register(r'boncommandes', BonCommandeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Ajoutez le routeur de l'application stock sous le préfixe "api/stock/"
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/stock/', include(stock_router.urls)),
    path('accounts/', include('authentification.urls')), 
    path('test_token/', views.test_token),
]




