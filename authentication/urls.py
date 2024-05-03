from django.urls import path
from .views import *

urlpatterns = [
    path('generate-token', GenerateTokenViews.as_view(), name='generate-token'),
]
