from django.urls import path
from .views import HotWheelsModelListAPIView

urlpatterns = [
    path('models/', HotWheelsModelListAPIView.as_view(), name='model-list'),
]