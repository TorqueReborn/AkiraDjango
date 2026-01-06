from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate

@api_view(['GET'])
def test_api(request):
    return Response({
        'message': 'Test API is working!',
        'status': 'success'
    })

@api_view(['GET'])
def set_cookie(request):
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

@api_view(['POST'])
def create_session(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    if user is None:
        return Response(
            {'error': 'Invalid username or password'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    return Response({'message': 'This is create session'})