from rest_framework import serializers
from medicine.models import MedicineModel
from django.contrib.auth.models import User

class MedicineSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicineModel
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length = 20)
    email = serializers.CharField(max_length = 20)
    password = serializers.CharField(max_length = 20)

    class Meta:
        model = User
        fields = ('username','email','password')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user