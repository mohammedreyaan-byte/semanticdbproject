from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SemanticModel


#Health Endpoint

@api_view(['GET'])

def health_endpoint(request):
    return Response({'status': 'ok'},status=status.HTTP_200_OK)

