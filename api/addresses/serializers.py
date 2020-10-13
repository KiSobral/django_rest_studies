from rest_framework.serializers import ModelSerializer
from .models import Adress


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Adress
        fields = ('id', 'line1', 'line2', 'city', 'state', 'country')
