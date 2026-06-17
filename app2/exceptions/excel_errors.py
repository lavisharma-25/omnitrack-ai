from app.exceptions.base import (
    TrackFlowException,
    ResourceNotFoundException,
    ResourceAlreadyExistsException,
)


class TrackerNotFoundError(ResourceNotFoundException):
    """
    Raised when tracker file does not exist.
    """

    def __init__(self, tracker_name: str):
        super().__init__(
            f"Tracker '{tracker_name}' does not exist."
        )


class TrackerAlreadyExistsError(ResourceAlreadyExistsException):
    """
    Raised when creating an existing tracker.
    """

    def __init__(self, tracker_name: str):
        super().__init__(
            f"Tracker '{tracker_name}' already exists."
        )


class RecordNotFoundError(ResourceNotFoundException):
    """
    Raised when record cannot be located.
    """

    def __init__(self, record_id: str):
        super().__init__(
            f"Record '{record_id}' not found."
        )


class InvalidTrackerSchemaError(TrackFlowException):
    """
    Raised when tracker schema is invalid.
    """

    def __init__(self, tracker_name: str):
        super().__init__(
            message=f"Tracker '{tracker_name}' has an invalid schema.",
            error_code="INVALID_TRACKER_SCHEMA",
        )


class ExcelOperationError(TrackFlowException):
    """
    Raised when Excel read/write operations fail.
    """

    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="EXCEL_OPERATION_ERROR",
        )