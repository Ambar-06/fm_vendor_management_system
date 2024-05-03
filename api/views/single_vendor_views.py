from api.serializers.vendor_detail_serializers import SingleVendorDetailSerializer
from api.serializers.vendors_serializer import VendorsViewSerializer
from api.services.single_vendor_services import SingleVendorServices
from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request


class SingleVendorViews(BaseAPIView):
    
    def __init__(self):
        self.service = SingleVendorServices()
    
    @validate_request(SingleVendorDetailSerializer)
    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(VendorsViewSerializer(response_data).data, status_code)
    
    @validate_request(SingleVendorDetailSerializer)
    @auth_guard()
    def put(self, request, data, *args):
        service_data = self.service.update_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(VendorsViewSerializer(response_data).data, status_code)
    
    @validate_request(SingleVendorDetailSerializer)
    @auth_guard()
    def delete(self, request, data, *args):
        service_data = self.service.delete_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(response_data, status_code)
