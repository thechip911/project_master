# django import
from django.urls import path

# app label
from accounts.views import UserDashBoard, UserLoginView, UserLogoutView, UserSignUpView

# local view import

app_name = 'accounts'

urlpatterns = [
    path('user_dashboard/', UserDashBoard.as_view(), name='user_dashboard'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]
