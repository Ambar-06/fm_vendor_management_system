from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from orders.serializers.single_po_serializers import SinglePurchaseOrderFilterSerializer
from orders.services.single_po_services import SinglePurchaseOrderService


class SinglePurchaseOrderView(BaseAPIView):
    def __init__(self):
        self.service = SinglePurchaseOrderService()

    @validate_request(SinglePurchaseOrderFilterSerializer)
    @auth_guard()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(response_data, status_code)
    
    @auth_guard()
    @validate_request(SinglePurchaseOrderFilterSerializer)
    def put(self, request, data, *args):
        service_data = self.service.update_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(response_data, status_code)
    
    @auth_guard()
    @validate_request(SinglePurchaseOrderFilterSerializer)
    def delete(self, request, data, *args):
        service_data = self.service.delete_service(request, data)
        response_data = service_data.get("response_data")
        status_code = service_data.get("code")
        return self.success(response_data, status_code)
    