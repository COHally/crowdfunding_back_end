from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Get or create the token associated with the user
        token, created = Token.objects.get_or_create(user=user)

        # Customize the response with additional user details if needed
        custom_response = {
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email,
            # Add more user details as necessary
        }

        return Response(custom_response)