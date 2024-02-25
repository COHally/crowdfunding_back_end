from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # Call super to get the token
        response = super().post(request, *args, **kwargs)

        if 'token' in response.data:
            # Extract token from the response
            token = response.data['token']

            # Extract user details
            user_id = request.user.id if request.user else None
            user_email = request.user.email if request.user else None
            user_first_name = request.user.first_name if request.user else None
            user_last_name = request.user.last_name if request.user else None

            # add more user details to response as needed
            custom_response = {
                'token': token,
                'user_id': user_id,
                'email': user_email,
                'first_name': user_first_name,
                'last_name': user_last_name
            }

            return Response(custom_response)

        return response