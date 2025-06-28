from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import UserProfile
from .serializers import (
    UserSerializer, UserProfileSerializer, RegisterSerializer, ChangePasswordSerializer
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer
    
    def get_object(self):
        return self.request.user.profile


class ChangePasswordView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer
    
    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.user
        
        # Check old password
        if not user.check_password(serializer.data.get('old_password')):
            return Response({'old_password': ['Wrong password.']}, status=status.HTTP_400_BAD_REQUEST)
        
        # Set new password
        user.set_password(serializer.data.get('new_password'))
        user.save()
        
        return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    """Get current user information"""
    user_serializer = UserSerializer(request.user)
    profile_serializer = UserProfileSerializer(request.user.profile)
    
    return Response({
        'user': user_serializer.data,
        'profile': profile_serializer.data
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def check_username(request):
    """Check if username is available"""
    username = request.data.get('username')
    if not username:
        return Response({'error': 'Username is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    exists = User.objects.filter(username=username).exists()
    return Response({'available': not exists})


@api_view(['POST'])
@permission_classes([AllowAny])
def check_email(request):
    """Check if email is available"""
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)
    
    exists = User.objects.filter(email=email).exists()
    return Response({'available': not exists}) 