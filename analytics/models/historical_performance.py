from common.models.base_model import BaseModel
from vendor.models.vendor import Vendor
from django.db import models


class HistoricalPerformance(BaseModel):
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField()
    quality_rating_avg = models.FloatField()
    on_time_delivery_rate = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()