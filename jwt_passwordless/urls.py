from jwt_passwordless.settings import api_settings
from django.urls import path, include
from jwt_passwordless.views import (
     ObtainEmailCallbackToken,
     ObtainMobileCallbackToken,
     ObtainAuthTokenFromCallbackToken,
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView


app_name = 'jwt_passwordless'

urlpatterns = [
     path(api_settings.PASSWORDLESS_AUTH_PREFIX + 'email/', ObtainEmailCallbackToken.as_view(), name='auth_email'),
     path(api_settings.PASSWORDLESS_AUTH_PREFIX + 'mobile/', ObtainMobileCallbackToken.as_view(), name='auth_mobile'),
     path(api_settings.PASSWORDLESS_AUTH_PREFIX + 'token/', ObtainAuthTokenFromCallbackToken.as_view(), name='auth_token'),
     path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
     path('jwt/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),   
]
