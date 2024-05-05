from django.db import models
from common.models.base_model import BaseModel
from vendor.models.vendor import Vendor


class PurchaseOrder(BaseModel):

    STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    po_number = models.CharField(max_length=255, db_index=True, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=255, choices=STATUS, default='pending')
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)