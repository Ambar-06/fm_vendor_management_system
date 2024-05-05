from rest_framework import serializers

class PurchaseOrderFilterSerializer(serializers.Serializer):
    
    vendorId = serializers.CharField(required=False, allow_blank=True, allow_null=True)