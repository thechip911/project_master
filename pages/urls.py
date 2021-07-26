# django import
from django.urls import path

# local view import

# app label
from pages.views import HomePageView

app_name = 'pages'

urlpatterns = [
    # login/logout related urls
    path('', HomePageView.as_view(), name='homepage'),

]
