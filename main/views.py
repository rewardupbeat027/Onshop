from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Product, ProductImage, Comment, Rating
from .permission import Editor
from .serializers import ProductSerializer, ProductImageSerializer, CommentSerializer, RatingSerializer, ProfileSerializer


# Create your views here.
class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []

class ProductImageAPIView(generics.ListAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    permission_classes = []

class CommentAPIView(generics.ListCreateAPIView, generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = []


class RatingAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = []


class EditorViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [Editor]


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            data = {
                "user_id": user.id,
                "message": "User registered successfully."
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
