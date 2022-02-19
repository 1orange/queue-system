from rest_framework.serializers import ValidationError
from rest_framework import status


class ReasonNotFound(ValidationError):
    """
    raises API exceptions with custom messages and custom status codes
    """

    status_code = status.HTTP_404_NOT_FOUND
    default_code = 'error'

    def __init__(self, status_code=None):
        self.detail = "No reason has been found."

        if status_code is not None:
            self.status_code = status_code
