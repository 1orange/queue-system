from rest_framework.response import Response
from rest_framework import status


def InvalidRequest(detail=None, response=None):
    if not response:
        response = status.HTTP_400_BAD_REQUEST

    if not detail:
        detail = "Invalid request ..."

    return Response(
        {
            "reason": detail
        },
        status=response
    )