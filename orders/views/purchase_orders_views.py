from orders.services.purchase_orders_service import PurchaseOrdersService
from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard


class PurchaseOrdersViews(BaseAPIView):
    
    def __init__(self):
        self.service = PurchaseOrdersService()

    @auth_guard()
    def get(self, request, *args):
        service_data = self.service.get_service()
        response_data = service_data.get('response_data')
        status_code = service_data.get('code')
        return self.success(response_data, status_code)