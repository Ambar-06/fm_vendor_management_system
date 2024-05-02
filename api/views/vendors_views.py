from api.services.vendors_service import VendorsService
from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.decorators.validate_request import validate_request


class VendorsViews(BaseAPIView):
    def __init__(self):
        self.service = VendorsService()

    @validate_request()
    def get(self, request, data, *args):
        pass