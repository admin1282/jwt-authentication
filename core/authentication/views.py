from django.shortcuts import render
from .models import AppUser, Profile
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer, LoginSerializer, ProfileSerializer
# Create your views here.


class RegisterCreateView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []


class LoginAPIView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = []


class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]