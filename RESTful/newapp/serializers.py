from rest_framework import serializers
from newapp.models import NewUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ['id', 'name', 'username', 'email']