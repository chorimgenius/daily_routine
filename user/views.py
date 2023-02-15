from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.models import User
from user.serializers import CustomUserserializer, CustomObtainPairSerializer

class UserView(APIView):
    #회원가입
    def post(self, request):
        serializer = CustomUserserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "회원가입을 축하합니다!"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message" : f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomObtainPairSerializer