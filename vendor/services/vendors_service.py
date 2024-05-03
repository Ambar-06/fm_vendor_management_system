from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from common.helpers.unique_code_generator import UniqueCodeGenerator
from vendor.repositories.vendor_repo import VendorRepository


class VendorsService(BaseService):
    def __init__(self):
        self.vendor_repo = VendorRepository()

    def get_service(self):
        vendors_data = self.vendor_repo.GetAll([], error=False)
        return self.ok(vendors_data, StatusCodes().SUCCESS)

    def post_service(self, request, data):
        values = {
            "name": data.get("name"),
            "contact_details": data.get("contactDetails"),
            "address": data.get("address"),
            "vendor_code" : UniqueCodeGenerator().generate_random_code(use_alphanumeric=True),
        }
        vendor_data = self.vendor_repo.Create(values)
        return self.ok(vendor_data, StatusCodes().CREATED)