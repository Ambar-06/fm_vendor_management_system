from common.boilerplate.decorators.validate_request import validate_request
from orders.serializers.purchase_orders_serializers import PurchaseOrderFilterSerializer
from orders.services.purchase_orders_service import PurchaseOrdersService
from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard


class PurchaseOrdersViews(BaseAPIView):
    
    def __init__(self):
        self.service = PurchaseOrdersService()

    @auth_guard()
    @validate_request(PurchaseOrderFilterSerializer)
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response_data = service_data.get('response_data')
        status_code = service_data.get('code')
        return self.success(response_data, status_code)
    
    def post(self, request, data, *args):
        service_data = self.service.post_service(request.data)
        response_data = service_data.get('response_data')
        status_code = service_data.get('code')
        return self.success(response_data, status_code)