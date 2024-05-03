from api.util.single_vendor_request_validator import SingleVendorRequestValidator
from common.boilerplate.services.base_service import BaseService
from common.helpers.constants import StatusCodes
from vendor.repositories.vendor_repo import VendorRepository
from rest_framework import exceptions


class SingleVendorServices(BaseService):

    def __init__(self):
        self.vendor_repo = VendorRepository()
        self.validator = SingleVendorRequestValidator()

    def get_service(self, request, data):
        vendor_data = self.vendor_repo.GetFirst(
            [("uuid", data.get("vendorId"))], error=False
        )
        if not vendor_data:
            raise exceptions.NotFound("Vendor not found")
        return self.ok(vendor_data, StatusCodes().SUCCESS)

    def update_service(self, request, data):
        request, data = self.validator.validate_request(request, data)
        vendor_data = self.vendor_repo.GetFirst(
            [("uuid", data.get("vendorId"))], error=False
        )

        if not vendor_data:
            raise exceptions.NotFound("Vendor not found")

        vendor_data.name = data.get("name") if data.get("name") else vendor_data.name
        vendor_data.contact_details = (
            data.get("contactDetails")
            if data.get("contactDetails")
            else vendor_data.contact_details
        )
        vendor_data.address = (
            data.get("address") if data.get("address") else vendor_data.address
        )
        vendor_data.save()
        return self.ok(vendor_data, StatusCodes().SUCCESS)

    def delete_service(self, request, data):
        vendor_data = self.vendor_repo.GetFirst(
            [("uuid", data.get("vendorId"))], error=False
        )
        if not vendor_data:
            raise exceptions.NotFound("Vendor not found")
        vendor_data.is_deleted = True
        vendor_data.save()
        return self.ok("Vendor has been deleted.", StatusCodes().SUCCESS)
