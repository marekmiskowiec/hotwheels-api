from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HotWheelsModel
from .serializers import HotWheelsModelSerializer

class HotWheelsModelListAPIView(APIView):
    def get(self, request):
        models = HotWheelsModel.objects.all()
        serializer = HotWheelsModelSerializer(models, many=True)
        return Response(serializer.data)