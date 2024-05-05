from rest_framework import serializers


class SinglePurchaseOrderFilterSerializer(serializers.Serializer):

    purchaseOrderId = serializers.UUIDField(
        required=True,
        allow_null=False,
        allow_blank=False,
        error_messages={
            "required": "Purchase Order Id is required",
            "invalid": "Purchase Order Id is invalid",
            "null": "Purchase Order Id is invalid",
            "blank": "Purchase Order Id is invalid",
        },
    )
    vendorId = serializers.UUIDField(required=False, allow_null=True, allow_blank=True)
    orderDate = serializers.DateTimeField(required=False, allow_null=True)
    deliveryDate = serializers.DateTimeField(required=False, allow_null=True)
    status = serializers.ChoiceField(required=False, allow_null=True, choices=["pending", "completed", "canceled"])
    quantity = serializers.IntegerField(required=False, allow_null=True)
    issueDate = serializers.DateTimeField(required=False, allow_null=True)
    acknowledgmentDate = serializers.DateTimeField(required=False, allow_null=True)
