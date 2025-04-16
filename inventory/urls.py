from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StockItemViewSet, UnitViewSet

router = DefaultRouter()
router.register(r'stock-items', StockItemViewSet)
router.register(r'units', UnitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
