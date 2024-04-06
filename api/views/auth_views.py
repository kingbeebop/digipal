# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers import UserSerializer, RegistrationSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User created successfully'})
        else:
            return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        # Your login logic here
        # Authenticate user and generate access and refresh tokens
        return Response({'message': 'Login successful'})

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # Your logout logic here
        # Invalidate tokens or add them to blacklist
        return Response({'message': 'Logout successful'})

class RefreshTokenView(APIView):
    def post(self, request):
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)

        response_data = {
            'access_token': str(token.access_token),
        }
        return Response(response_data)

class GetUserDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

