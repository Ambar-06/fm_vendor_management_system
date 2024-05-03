from vendor.serializers.vendors_serializer import VendorCreationSerializer, VendorsViewSerializer
from vendor.services.vendors_service import VendorsService
from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request


class VendorsViews(BaseAPIView):
    def __init__(self):
        self.service = VendorsService()

    @auth_guard()
    def get(self, request, *args):
        service_data = self.service.get_service()
        response_data = service_data.get('response_data')
        status_code = service_data.get('code')
        return self.success(VendorsViewSerializer(response_data, many=True).data, status_code)
    
    
    @validate_request(VendorCreationSerializer)
    @auth_guard()
    def post(self, request, data, *args):
        service_data = self.service.post_service(request, data)
        response_data = service_data.get('response_data')
        status_code = service_data.get('code')
        return self.success(VendorsViewSerializer(response_data).data, status_code)