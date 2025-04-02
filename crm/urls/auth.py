from django.urls import path
from crm.views.auth import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # POST /auth/register/
    path('login/', LoginView.as_view(), name='login'),  # POST /auth/login/
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # POST /auth/refresh/
]

