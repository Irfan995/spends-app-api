from django.urls import path, include
from spends import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'spends', views.SpendViewSet)

urlpatterns = [
     path('', include(router.urls)),
]
