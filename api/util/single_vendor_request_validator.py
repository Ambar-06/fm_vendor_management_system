from rest_framework.serializers import ValidationError

class SingleVendorRequestValidator:
    
    def __init__(self):
        pass

    def validate_request(self, request, data):

        if data.get("name").strip() == "" if data.get("name") is not None else False:
            data["name"] = None

        if data.get("contactDetails").strip() == "" if data.get("contactDetails") is not None else False:
            data["contactDetails"] = None

        if data.get("address").strip() == "" if data.get("address") is not None else False:
            data["address"] = None
        
        return request, data
            