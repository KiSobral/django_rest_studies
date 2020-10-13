from rest_framework.viewsets import ModelViewSet
from .models import Adress
from .serializers import AddressSerializer


class AddressViewsets(ModelViewSet):
    queryset = Adress.objects.all()
    serializer_class = AddressSerializer
