from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from orders.repositories.purchase_orders_repo import PurchaseOrderRepository
from rest_framework import exceptions
from orders.util.single_po_request_validator import SinglePurchaseOrderRequestValidator
from orders.util.update_po_helper import PurchaseOrderHelper


class SinglePurchaseOrderService(BaseService):
    def __init__(self):
        self.po_repo = PurchaseOrderRepository()
        self.request_validator = SinglePurchaseOrderRequestValidator()
        self.helper = PurchaseOrderHelper()

    def get_service(self, request, data):
        po_data = self.po_repo.GetFirst(
            [("uuid", data.get("purchaseOrderId"))], error=False
        )
        return self.ok(po_data, StatusCodes().SUCCESS)
    
    def update_service(self, request, data):
        request, data = self.request_validator.validate_request(request, data)
        po_data = self.po_repo.GetFirst(
            [("uuid", data.get("purchaseOrderId"))], error=False
        )
        if not po_data:
            raise exceptions.NotFound("Purchase Order not found")
        po_data = self.helper.update_purchase_order(po_data, data)
        return self.ok(po_data, StatusCodes().SUCCESS)
    
    def delete_service(self, request, data):
        po_data = self.po_repo.GetFirst(
            [("uuid", data.get("purchaseOrderId"))], error=False
        )
        if not po_data:
            raise exceptions.NotFound("Purchase Order not found")
        po_data.is_deleted = True
        po_data.save()
        return self.ok("Purchase Order has been deleted.", StatusCodes().SUCCESS)
