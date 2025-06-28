from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'name', 'email', 'date_joined', 'department']
        read_only_fields = ['has_company_card']  # Encapsulation

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'name', 'email', 'date_joined', 'mentor', 'internship_end']
