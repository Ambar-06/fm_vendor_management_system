from dataclasses import dataclass


@dataclass
class StatusCodes(object):
    def __init__(self):
        self.SUCCESS = 200
        self.CREATED = 201
        self.NO_CONTENT = 204
        self.BAD_REQUEST = 400
        self.UNAUTHORIZED = 401
        self.FORBIDDEN = 403
        self.NOT_FOUND = 404
        self.UNPROCESSABLE_ENTITY = 422
        self.INTERNAL_SERVER_ERROR = 500
        self.BAD_GATEWAY = 502
        self.SERVICE_UNAVAILABLE = 503


obj_status_codes = StatusCodes()
StatusCodesDictionary = obj_status_codes.__dict__

@dataclass
class DateInputFormats(object):
    def __init__(self):
        self.DATE = "%Y-%m-%d"
        self.DATETIME = "%Y-%m-%d %H:%M:%S"