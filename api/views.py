from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
from drf_yasg.utils import swagger_auto_schema
from django.http import Http404

class MessageView(APIView):
    serializer_class = MessageSerializer

    @swagger_auto_schema(responses={200: MessageSerializer(many=True)})
    def get(self, request):
        messages = Message.objects.all()
        serializer = self.serializer_class(messages, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MessageSerializer)
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MessageDetailView(APIView):
    serializer_class = MessageSerializer

    def get_object(self, pk):
        try:
            return Message.objects.get(pk=pk)
        except Message.DoesNotExist:
            raise Http404

    @swagger_auto_schema(responses={200: MessageSerializer})
    def get(self, request, pk):
        message = self.get_object(pk)
        serializer = self.serializer_class(message)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=MessageSerializer)
    def put(self, request, pk):
        message = self.get_object(pk)
        serializer = self.serializer_class(message, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        message = self.get_object(pk)
        message.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

