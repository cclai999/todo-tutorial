from typing import Optional, Any


class AppException(Exception):
    message: Any = ""
    status_code: int = 400

    def __init__(self, message: Any = None, status_code: int = None, *args):
        super(AppException, self).__init__(message, status_code, *args)
        if message is not None:
            self.message = message
        if status_code is not None:
            self.status_code = status_code

    def __str__(self):
        return f"<APIException: {self.message=} {self.status_code=}>"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "message": self.message,
            "status_code": self.status_code,
            "result": False
        }


class DatabaseOperationError(AppException):
    status_code = 500
    message = "Database operation failed"
    exc_val: Optional[Exception] = None

    def __init__(self, message, status_code=None, exc_val=None):
        self.message = message
        self.status_code = status_code or self.status_code
        self.exc_val = exc_val

    def to_dict(self):
        response = super().to_dict()
        response["detail"] = str(self.exc_val.args[0])
        return response
