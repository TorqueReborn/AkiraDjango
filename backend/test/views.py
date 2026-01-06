from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def test_api(request):
    return Response({
        'message': 'Test API is working!',
        'status': 'success'
    })

@api_view(['GET'])
def cookie(request):
    response = Response(
        {'message': 'This is cookie response'}
    )
    response.set_cookie(
            key='token',
            value='This is a token',
            samesite='None',
            secure=True
        )
    return response