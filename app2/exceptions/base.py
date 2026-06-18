from typing import Any


class TrackFlowException(Exception):
    """
    Base exception for all TrackFlow AI errors.
    """

    def __init__(
        self,
        message: str,
        error_code: str = "TRACKFLOW_ERROR",
        details: Any = None,
    ):
        self.message = message
        self.error_code = error_code
        self.details = details

        super().__init__(message)

    def to_dict(self) -> dict:
        return {
            "error_code": self.error_code,
            "message": self.message,
            "details": self.details,
        }


class ValidationException(TrackFlowException):
    """
    Raised when input validation fails.
    """

    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="VALIDATION_ERROR",
        )


class ResourceNotFoundException(TrackFlowException):
    """
    Raised when a requested resource does not exist.
    """

    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="RESOURCE_NOT_FOUND",
        )


class ResourceAlreadyExistsException(TrackFlowException):
    """
    Raised when a resource already exists.
    """

    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="RESOURCE_ALREADY_EXISTS",
        )