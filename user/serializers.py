from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from user.models import User
import re 


class CustomUserserializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"

    def validate_password(self, value):
        pattern = r'^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z]).{8,}$'
        if not re.search(pattern, value):
            raise serializers.ValidationError('비밀번호는 8글자 이상이며 특수문자, 숫자를 포함해야 합니다.')
        return value
        
class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        return token
        