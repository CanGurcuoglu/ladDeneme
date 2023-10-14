from rest_framework import serializers
from missions.models import User, Mission

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        #fields = '__all__'
        exclude = ['user']

class UserSerializer(serializers.ModelSerializer):
    missions = MissionSerializer(many = True, read_only = True)
    class Meta:
        model = User
        fields = '__all__'