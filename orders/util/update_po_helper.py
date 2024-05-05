from orders.repositories.purchase_orders_repo import PurchaseOrderRepository


class PurchaseOrderHelper:
    def __init__(self):
        self.po_repo = PurchaseOrderRepository()

    def update_purchase_order(self, po_data, data):
        vendor_ins = self.vendor_repo.GetFirst([("uuid", data.get("vendorId"))], error=False)
        po_data.vendor = vendor_ins if data.get("vendorId") else po_data.vendor
        po_data.order_date = data.get("orderDate") if data.get("orderDate") else po_data.order_date
        po_data.delivery_date = data.get("deliveryDate") if data.get("deliveryDate") else po_data.delivery_date
        po_data.status = data.get("status") if data.get("status") else po_data.status
        po_data.quantity = data.get("quantity") if data.get("quantity") else po_data.quantity
        po_data.issue_date = data.get("issueDate") if data.get("issueDate") else po_data.issue_date
        po_data.acknowledgment_date = data.get("acknowledgmentDate") if data.get("acknowledgmentDate") else po_data.acknowledgment_date
        po_data.save()
        return po_data