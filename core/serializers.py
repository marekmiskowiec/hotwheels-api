from rest_framework import serializers
from .models import HotWheelsModel

class HotWheelsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotWheelsModel
        fields = '__all__'