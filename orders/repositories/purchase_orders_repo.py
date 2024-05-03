from common.boilerplate.db.base_repository import BaseRepository
from orders.models.purchase_order import PurchaseOrder


class PurchaseOrderRepository(BaseRepository):
    def __init__(self):
        self.model = PurchaseOrder