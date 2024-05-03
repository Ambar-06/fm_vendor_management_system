from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from orders.repositories.purchase_orders_repo import PurchaseOrderRepository


class PurchaseOrdersService(BaseService):
    def __init__(self):
        self.po_repo = PurchaseOrderRepository()

    def get_service(self):
        purchase_orders_data = self.po_repo.GetAll([], error=False)
        return self.ok(purchase_orders_data, StatusCodes().SUCCESS)