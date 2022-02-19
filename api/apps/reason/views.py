import http

from rest_framework.response import Response

from .models import MedicalReason
from .serializers import MedicalReasonSerializer
from http import HTTPStatus

from rest_framework import status

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view

from drf_spectacular.utils import extend_schema

from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from api.apps.helpers.serializers import GenericResponseSerializer

from rest_framework import generics


class ReasonsListView(APIView):
    """
    List all available reasons for visitation.
    """

    @extend_schema(
        request=None,
        responses={
            200: MedicalReasonSerializer(many=True),
            400: GenericResponseSerializer,
            405: GenericResponseSerializer,
        }
    )
    def get(self, request):
        reasons = MedicalReason.objects.all()
        serializer = MedicalReasonSerializer(reasons, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
