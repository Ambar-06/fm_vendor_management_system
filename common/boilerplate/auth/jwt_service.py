from jose import jwt
from datetime import datetime, timedelta
from vendor_management_system import settings

"""
This class is used for JWT
Fields:
    JWT_SECRET: Secret for JWT
Methods:
    create_token: This method is used for creating a new JWT token
    verify_token: This method is used for verifying a JWT token
WorkFlow:
    First we create a payload
    Then we create a token
    Then we return the token
"""


class JWTService:
    JWT_SECRET = settings.JWT_SECRET

    def create_token(self):
        payload = {
            "sub": str(settings.JWT_CUSTOM_STRING),
            "iat": datetime.now(),
            "exp": datetime.now() + timedelta(days=int(settings.JWT_EXP_DELTA_DAYS)),
        }
        token = jwt.encode(payload, JWTService.JWT_SECRET, settings.JWT_ALGORITHM)
        return token

    def verify_token(self, jwt_token):
        jwt_payload = jwt.decode(
            jwt_token, JWTService.JWT_SECRET, settings.JWT_ALGORITHM
        )
        return jwt_payload
