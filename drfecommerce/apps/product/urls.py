from rest_framework import routers
from django.urls import path
from .views import *

router = routers.DefaultRouter()

router.register(r'category', CategoryViewSet)
router.register(r'brand', BrandViewSet)
router.register(r'product', ProductViewSet)


urlpatterns = [
    
]

urlpatterns += router.urls
