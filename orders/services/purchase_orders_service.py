from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from common.helpers.unique_code_generator import UniqueCodeGenerator
from orders.repositories.purchase_orders_repo import PurchaseOrderRepository
from rest_framework import exceptions
import datetime as dt

from vendor.repositories.vendor_repo import VendorRepository


class PurchaseOrdersService(BaseService):
    def __init__(self):
        self.po_repo = PurchaseOrderRepository()
        self.vendor_repo = VendorRepository()

    def get_service(self, request, data):
        if data.get("vendorId") is not None and data.get("vendorId") != "":
            purchase_orders_data = self.po_repo.GetAll([("vendor__uuid", data.get("vendorId"))], error=False)
        else:  
            purchase_orders_data = self.po_repo.GetAll([], error=False)
        return self.ok(purchase_orders_data, StatusCodes().SUCCESS)
    
    def post_service(self, data):
        vendor_ins = self.vendor_repo.GetFirst([("uuid", data.get("vendorId"))], error=False)
        if vendor_ins is None:
            raise exceptions.ValidationError({"vendorId": "Vendor not found"})
        values = {
            "po_number": UniqueCodeGenerator().generate_random_code(use_alphanumeric=True),
            "vendor": vendor_ins,
            "order_date": data.get("orderDate"),
            "delivery_date": data.get("deliveryDate"),
            "items": data.get("items"),
            "quantity": data.get("quantity"),
            "status": "pending",
            "issue_date": dt.datetime.now(),
        }
        purchase_order_data = self.po_repo.Create(values)
        return self.ok(purchase_order_data, StatusCodes().CREATED)