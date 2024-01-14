from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.serializers import UserSerializer


@api_view(['POST',])
def account_registration(request):
    user_data = request.data.get('user')

    serializer = UserSerializer(data=user_data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({'user': serializer.data},
                    status=status.HTTP_201_CREATED)


@api_view(['POST',])
def account_login(request):
    user_data = request.data.get('user')
    user = authenticate(
        email=user_data['email'], password=user_data['password'])
    serializer = UserSerializer(user)
    jwt_token = RefreshToken.for_user(user)
    serializer_data = serializer.data
    serializer_data['token'] = str(jwt_token.access_token)
    response_data = {
        'user': serializer_data,
    }
    return Response(response_data, status=status.HTTP_202_ACCEPTED)
