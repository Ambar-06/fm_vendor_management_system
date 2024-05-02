from rest_framework import serializers

class SingleVendorDetailSerializer(serializers.ModelSerializer):
    
    vendorId = serializers.CharField(required=True, allow_blank=False, allow_null=False, error_messages={
        "required": "Vendor ID is required",
        "blank": "Vendor ID cannot be blank",
        "null": "Vendor ID cannot be null",
    })
    name = serializers.CharField(
        required=True,
        allow_null=True,
    )
    contactDetails = serializers.CharField(
        required=False,
        allow_null=True,
    )
    address = serializers.CharField(
        required=False,
        allow_null=True,
    )