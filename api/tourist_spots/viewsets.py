from rest_framework.viewsets import ModelViewSet
from .models import TouristSpot
from .serializers import TouristSpotSerializer


class TouristSpotViewsets(ModelViewSet):
    serializer_class = TouristSpotSerializer

    def get_queryset(self):
        return TouristSpot.objects.filter(approvedd=True)
