from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response

# Create your views here.

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'message': 'User registered  successfully',
            
            }
        return Response(response, status=status_code)

