from django.urls import path

from .views import *

urlpatterns = [
    path('get-auth-token', GenerateTokenViews.as_view(), name='get_auth_token'),
]
