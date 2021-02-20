from rest_framework import serializers
from .models import CoffeeMachine, CoffeePod


class ListCoffeeMachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeeMachine
        fields = [
            "name"
        ]


class ListCoffeePodSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoffeePod
        fields = [
            "name"
        ]
