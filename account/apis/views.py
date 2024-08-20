from rest_framework.decorators import api_view
from .serializers import SignUpSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status



@api_view(['POST'],)
def logout_view(request):
    
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)



@api_view(['POST'],)

def signup_view(request):

    if request.method == 'POST':
        serializer = SignUpSerializer(data=request.data)

        data = {}


        if serializer.is_valid():

            account = serializer.save()


            data['response'] = "user signup successfully."
            data['username'] = account.username
            data['email'] = account.email
            token = Token.objects.get(user=account).key
            data['token'] = token
        
        else:
            data = serializer.errors
        
        return Response(data)