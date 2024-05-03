from django.db import models
from common.models.base_model import BaseModel


class Vendor(BaseModel):

    name = models.CharField(max_length=255, db_index=True)
    contact_details = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    vendor_code = models.CharField(max_length=16, db_index=True, unique=True)
    on_time_delivery_rate = models.FloatField(db_index=True, default=0.0)
    quality_rating_avg = models.FloatField(db_index=True, default=0.0)
    average_response_time = models.FloatField(db_index=True, default=0.0)
    fulfillment_rate = models.FloatField(db_index=True, default=0.0)
    