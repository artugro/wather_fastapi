from fastapi import HTTPException, status


class APIException(HTTPException):
    """
    Generic exceptions for errors
    """

    def __init__(self):
        super().__init__(
            detail="Error processing your request",
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
