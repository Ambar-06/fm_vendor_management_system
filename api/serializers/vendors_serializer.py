from vendor.models.vendor import Vendor
from rest_framework import serializers


class VendorsViewSerializer(serializers.ModelSerializer):

    contactDetails = serializers.CharField(source="contact_details", read_only=True)
    vendorCode = serializers.CharField(source="vendor_code", read_only=True)
    onTimeDeliveryRate = serializers.FloatField(
        source="on_time_delivery_rate", read_only=True
    )
    qualityRatingAvg = serializers.FloatField(
        source="quality_rating_avg", read_only=True
    )
    averageResponseTime = serializers.FloatField(
        source="average_response_time", read_only=True
    )
    fulfillmentRate = serializers.FloatField(source="fulfillment_rate", read_only=True)

    class Meta:
        model = Vendor
        fields = [
            "id",
            "uuid",
            "name",
            "contactDetails",
            "address",
            "vendorCode",
            "onTimeDeliveryRate",
            "qualityRatingAvg",
            "averageResponseTime",
            "fulfillmentRate",
        ]


class VendorCreationSerializer(serializers.Serializer):

    name = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={
            "required": "Name is required",
            "blank": "Name cannot be blank",
            "null": "Name cannot be null",
        },
    )
    contactDetails = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={
            "required": "Contact Details is required",
            "blank": "Contact Details cannot be blank",
            "null": "Contact Details cannot be null",
        },
    )
    address = serializers.CharField(
        required=True,
        allow_blank=False,
        allow_null=False,
        error_messages={
            "required": "Address is required",
            "blank": "Address cannot be blank",
            "null": "Address cannot be null",
        },
    )
