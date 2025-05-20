from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json

@api_view(['POST'])
def calculate_sum(request):
    try:
        data = json.loads(request.body)
        num1 = int(data.get('num1', 0))
        num2 = int(data.get('num2', 0))


        result = num1 + num2

        return Response({
            'result' : result,
            'num1' : num1,
            'num2' : num2
        }, status = status.HTTP_200_OK)
    
    except (ValueError, TypeError) as e:
        return Response({
            'error' : 'Invalid input, Please provide valid integers.'
        }, status = status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({
            'error' : str(e)
        }, status = status.HTTP_500_INTERNAL_SERVER_ERROR)