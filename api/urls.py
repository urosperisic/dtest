from django.urls import path
from .views import PorukaView

urlpatterns = [
    path('poruke/', PorukaView.as_view(), name='poruke'),
]

