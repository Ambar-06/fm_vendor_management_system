from django.urls import path
from .views import *

urlpatterns = [
    path('', VendorsViews.as_view(), name='vendors'),
    path('<str:vendorId>/', SingleVendorViews.as_view(), name='single_vendor'),
]
