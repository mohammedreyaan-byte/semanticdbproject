from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .metricservice import calculate_metric
from .properties.semantic import SEMANTIC_MODEL


#Health Endpoint

@api_view(['GET'])

def health_endpoint(request):
    return Response({'status': 'ok'},status=status.HTTP_200_OK)


#Metric Input Function

@api_view(['GET'])

def metric_view(request):

    data = request.query_params.get('metric')

    if not data:
        return Response({'status': 'error'}, status=status.HTTP_400_BAD_REQUEST)



    try:
        metric_value = calculate_metric(data)
        return Response({
            "metric":data,
            "metric_value":metric_value
        })

    except ValueError as error:
        return Response({
            "error":str(error)
        },status=status.HTTP_400_BAD_REQUEST)


#Semantic View

@api_view(['GET'])

def semantic_view(request):
    return Response(SEMANTIC_MODEL)