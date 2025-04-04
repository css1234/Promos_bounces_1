from rest_framework import status
from rest_framework.response import Response


def custom_api_response(success=True, message="", data=None, count=None, status_code=status.HTTP_200_OK):
    """
    Standardized API response format.
    
    :param success: Boolean indicating request success.
    :param message: Custom message for response.
    :param data: Actual response data.
    :param count: Optional count for paginated responses.
    :param status_code: HTTP status code.
    :return: DRF Response object.
    """
    response_structure = {
        "success": success,
        "message": message,
        "data": data if data is not None else [],
    }
    
    if count is not None:
        response_structure["count"] = count  # Include count for paginated data

    return Response(response_structure, status=status_code)
