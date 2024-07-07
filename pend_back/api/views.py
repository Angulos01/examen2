from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListPendientesSerializer,CreatePendienteSerializer,UpdatePendienteSerializer,DeletePendienteSerializer
from .models import Pendientes

class CreatePendienteAPIView(generics.CreateAPIView):
    serializer_class = CreatePendienteSerializer
    http_method_names = ['get','post']

class UpdatePendienteAPIView(generics.UpdateAPIView):
    serializer_class = UpdatePendienteSerializer
    queryset = Pendientes.objects.all()

class DeletePendienteAPIView(generics.DestroyAPIView):
    serializer_class = DeletePendienteSerializer
    queryset=Pendientes.objects.all()

class ListPendienteAPIView(APIView):
    serializer_class = ListPendientesSerializer
    def get(self, request):
        queryset = Pendientes.objects.all()
        data = ListPendientesSerializer(queryset,many=True).data
        return Response(data)