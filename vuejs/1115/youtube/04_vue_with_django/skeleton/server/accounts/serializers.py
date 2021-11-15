from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    # readonly는 serialize에는 포함 x 출력에만 포함
    # writeonly는 serialize에는 포함 o 출력에는 포함 x
    password = serializers.CharField(write_only=True)
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')
