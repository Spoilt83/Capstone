from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Booking, Menu
from .serializers import BookingSerializer, MenuSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

class UserViewSet(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response("User deleted")


class BookingViewSet(APIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        booking = Booking.objects.get(id=pk)
        booking.delete()
        return Response("Booking deleted")
        
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
 