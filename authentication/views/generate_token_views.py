from common.boilerplate.api.base_api_view import BaseAPIView
from common.boilerplate.auth.jwt_service import JWTService
from common.helpers.constants import StatusCodes


class GenerateTokenViews(BaseAPIView):
    def __init__(self):
        self.service = JWTService()

    def get(self, request, *args):
        token = self.service.create_token()
        return self.success({"token": token}, StatusCodes().SUCCESS)

