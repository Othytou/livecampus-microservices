from rest_framework import serializers
from .models import CustomUser

class CustomUserSeializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'age', 'firstname', 'lastname')
