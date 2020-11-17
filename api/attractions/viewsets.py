from rest_framework.viewsets import ModelViewSet
from .models import Attraction
from .serializers import AttractionSerializer


class AttractionViewsets(ModelViewSet):
    queryset = Attraction.objects.all()
    serializer_class = AttractionSerializer

    def get_queryset(self):
        return Attraction.objects.all()
