from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from .serializers import (AuthSerializer, LoginSerializer)
from django.core.mail import send_mail
from django.conf import settings

class AuthView(APIView):
    """
    Sign up a user
    """
    permission_classes = (AllowAny,)
    renderer_classes = [JSONRenderer]

    def post(self, request):
        data = request.data
        serializer = AuthSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        # configure email
        user_email = data['email']
        subject = 'Welcome to Rachis.io'
        message = 'I\'m sure you will find what you like. Yay!'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user_email,]

        send_mail( subject, message, email_from, recipient_list )

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class LoginView(APIView):
    """
    Sign in a user
    """
    permission_classes = (AllowAny,)
    renderer_classes = [JSONRenderer]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        print(serializer)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

        