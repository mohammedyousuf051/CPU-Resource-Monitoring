from rest_framework.serializers import ModelSerializer
from .models import Utilisation


class UtilisationSerializer(ModelSerializer):
    class Meta:
        model= Utilisation
        fields=('date_time','cpu_usage','ram_usage',)