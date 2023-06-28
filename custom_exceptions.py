from typing import Any

from fastapi import HTTPException


class SettingsFileNotFoundError(Exception):
    """Raised when the settings.json file is not found."""

    pass


class LocationException(HTTPException):
    def __init__(self, status_code: int, error: Any):
        super().__init__(status_code, detail=error)
        self.error = error
