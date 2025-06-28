from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegisterView, UserProfileView, ChangePasswordView,
    get_user_info, check_username, check_email
)

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('auth/user-info/', get_user_info, name='user_info'),
    path('auth/check-username/', check_username, name='check_username'),
    path('auth/check-email/', check_email, name='check_email'),
    path('profile/', UserProfileView.as_view(), name='profile'),
] 