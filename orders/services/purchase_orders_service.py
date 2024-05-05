from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from common.helpers.unique_code_generator import UniqueCodeGenerator
from orders.repositories.purchase_orders_repo import PurchaseOrderRepository


class PurchaseOrdersService(BaseService):
    def __init__(self):
        self.po_repo = PurchaseOrderRepository()

    def get_service(self, request, data):
        if data.get("vendorId") is not None:
            purchase_orders_data = self.po_repo.GetAll([("vendor__uuid", data.get("vendorId"))], error=False)
        else:  
            purchase_orders_data = self.po_repo.GetAll([], error=False)
        return self.ok(purchase_orders_data, StatusCodes().SUCCESS)
    
    def post_service(self, data):
        values = {
            "po_number": UniqueCodeGenerator().generate_random_code(use_alphanumeric=True),
            "vendor": data.get("order_date"),
            "order_date": data.get("order_number"),
            "delivery_date": data.get("order_status"),
            "items": data.get("total_amount"),
            "quantity": data.get("tax"),
            "status": data.get("discount"),
            "quality_rating": data.get("shipping"),
            "issue_date": data.get("grand_total"),
            "acknowledgment_date": data.get("payment_status"),
        }
        purchase_order_data = self.po_repo.Create(data)
        return self.ok(purchase_order_data, StatusCodes().CREATED)