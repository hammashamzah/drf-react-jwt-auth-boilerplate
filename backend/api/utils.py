from core.serializers import UserSerializer

def my_jwt_response_handler(token, user=None, request=None):
    return {
        'token': token,
        'request': request.data,
        'user': UserSerializer(user, context={'request': request}).data
    }