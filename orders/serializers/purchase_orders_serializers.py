from rest_framework import serializers

from common.helpers.constants import DateInputFormats


class PurchaseOrderFilterSerializer(serializers.Serializer):

    vendorId = serializers.CharField(required=False, allow_blank=True, allow_null=True)


class PurchaseOrderSerializer(serializers.Serializer):

    vendorId = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={
            "required": "Vendor ID is required",
            "blank": "Vendor ID cannot be blank",
            "null": "Vendor ID cannot be null",
        },
    )
    orderDate = serializers.DateTimeField(required=True, input_formats=[DateInputFormats().DATETIME])
    deliveryDate = serializers.DateTimeField(required=True, input_formats=[DateInputFormats().DATETIME])
    items = serializers.JSONField(required=True)
    quantity = serializers.IntegerField(required=True, min_value=1)
