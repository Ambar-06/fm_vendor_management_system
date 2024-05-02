from django.urls import path
from .views import *

urlpatterns = [
    path('get-auth-token', GenerateTokenViews.as_view(), name='get_auth_token'),
    path('vendors/', VendorsViews.as_view(), name='vendors'),
    # path('vendors/<str:vendorId>/', SingleVendorViews.as_view(), name='single_vendor'),
]
