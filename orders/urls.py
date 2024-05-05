from django.urls import path
from .views import *

urlpatterns = [
    path('', PurchaseOrdersViews.as_view(), name='purchase_orders'),
]