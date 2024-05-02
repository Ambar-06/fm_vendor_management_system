from rest_framework.serializers import ValidationError

class SingleVendorRequestValidator:
    
    def __init__(self):
        pass

    def validate_request(self, request, data):

        if data.get("name").strip() == "":
            data["name"] = None

        if data.get("contactDetails").strip() == "":
            data["contactDetails"] = None

        if data.get("address").strip() == "":
            data["address"] = None
        
        return request, data
            