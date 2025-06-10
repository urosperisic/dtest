# from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Poruka
from .serializers import PorukaSerializer
from drf_yasg.utils import swagger_auto_schema

class PorukaView(APIView):
    serializer_class = PorukaSerializer

    @swagger_auto_schema(responses={200: PorukaSerializer(many=True)})
    def get(self, request):
        poruke = Poruka.objects.all()
        serializer = self.serializer_class(poruke, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=PorukaSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
