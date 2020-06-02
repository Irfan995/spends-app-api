from core.models import Spend
from rest_framework import viewsets
from spends.serializers import SpendSerializer
# Create your views here.

class SpendViewSet(viewsets.ModelViewSet):
     """
    API endpoint that allows users to be viewed or edited.
    """
     queryset = Spend.objects.all()
     serializer_class = SpendSerializer
