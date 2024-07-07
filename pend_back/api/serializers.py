from rest_framework import serializers
from .models import Pendientes

class ListPendientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendientes
        fields = [
            "id",
            "title",
            "description",
            "user",
            "timestamp",
            "priority",
            "state",
        ]

class CreatePendienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendientes
        fields = "__all__"


class UpdatePendienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendientes
        fields = "__all__"

class DeletePendienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pendientes
        fields = "__all__"