import typing as _
from rest_framework.response import Response
from jose import jwt
from common.boilerplate.auth.jwt_service import JWTService
from vendor_management_system import settings

"""
This class is used for validating the user
This class is inherited from BaseService
Fields:
    userRepo: Instance of UserRepository
Methods:
    validate_auth_user: This method is used for validating the user
WorkFlow:
    First we get the authorization header
    Then we check if the authorization header is present or not
    If the authorization header is not present then we raise an exception
    If the authorization header is present then we get the jwt token
    Then we check if the jwt token is present or not
    If the jwt token is not present then we raise an exception
    Then we verify the jwt token
    Then we check if the payload is present or not
    If the payload is not present then we raise an exception
    Then we check the sub from the payload
    If the sub does not match with the environment variable then we raise an exception
    Then we return the response
"""
NOT_VALID_TOKEN = Response(
    {
        "success": False,
        "code": 401,
        "message": "Please provide a valid authorization header",
    },
    status=401,
)


HEADER_NOT_FOUND = Response(
    {"success": False, "code": 401, "message": "Authorization header not present"},
    status=401,
)

EXPIRED_TOKEN = Response(
    {"success": False, "code": 408, "message": "Token is expired"}, status=408
)

WRONG_SIGNATURE = Response(
    {"success": False, "code": 401, "message": "Invalid signature"}, status=401
)


def auth_guard(roles=None):
    def validate_auth_user(fun: _.Callable):
        jwt_service = JWTService()
        secret_id = settings.JWT_CUSTOM_STRING

        def inner(*args, **kwargs):
            req = args[1]
            auth_header = req.headers.get("Authorization")
            if not auth_header:
                return HEADER_NOT_FOUND

            jwt_token = auth_header.replace("Bearer ", "")
            if not jwt_token:
                return NOT_VALID_TOKEN

            try:
                payload = jwt_service.verify_token(jwt_token)
            except jwt.ExpiredSignatureError:
                return EXPIRED_TOKEN
            except jwt.JWTError:
                return WRONG_SIGNATURE
            if not payload:
                return NOT_VALID_TOKEN

            sub: _.Optional[str] = payload.get("sub")
            if not sub or sub != secret_id:
                return NOT_VALID_TOKEN
            return fun(*args, payload, **kwargs)

        return inner

    return validate_auth_user
