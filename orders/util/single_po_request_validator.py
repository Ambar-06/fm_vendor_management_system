from rest_framework.exceptions import ValidationError

class SinglePurchaseOrderRequestValidator:
    def __init__(self):
        pass

    def validate_request(self, request, data):
        if data.get("vendorId") == "" if data.get("vendorId") is not None else False:
            data['vendorId'] = None
        if data.get("orderDate") == "" if data.get("orderDate") is not None else False:
            data['orderDate'] = None
        if data.get("deliveryDate") == "" if data.get("deliveryDate") is not None else False:
            data['deliveryDate'] = None
        if data.get("status") == "" if data.get("status") is not None else False:
            data['status'] = None
        if data.get("quantity") == "" if data.get("quantity") is not None else False:
            data['quantity'] = None
        if data.get("issueDate") == "" if data.get("issueDate") is not None else False:
            data['issueDate'] = None
        if data.get("acknowledgmentDate") == "" if data.get("acknowledgmentDate") is not None else False:
            data['acknowledgmentDate'] = None
        return request, data