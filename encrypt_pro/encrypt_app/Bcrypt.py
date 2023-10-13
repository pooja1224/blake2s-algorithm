from . import models,serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import bcrypt
class Usersignup(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        try:
                serializer = serializers.UserSerializer(data=request.data)
                if serializer.is_valid():
                    digest = bcrypt.hashpw(serializer.validated_data['password'].encode('utf-8'), bcrypt.gensalt())

                    serializer.validated_data['password'] = digest
                    serializer.validated_data['salt'] = "string"
                    serializer.save()
                return Response({'response_code': status.HTTP_200_OK,
                                 'message': "signed in succesfully",
                                 'status_flag': True,
                                 'status': "success",
                                 'error_details': None,
                                 'data':[]
                                })
        except Exception as error:
            return Response({'response_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                             'message': "cant register",
                             'status_flag': False,
                             'status': "Failed",
                             'error_details': str(error),
                             'data': []})


class Login(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = serializers.UserSerializer(data=request.data)
            if serializer.is_valid():
                user = models.User.objects.get(name=request.data['name'])
                serializer = serializers.UserSerializer(instance=user)
                p = request.data['password']
                if bcrypt.checkpw(p.encode('utf-8'),user.password):
                        data_response = {
                                'response_code': status.HTTP_200_OK,
                                'message': "logged in succesfully",
                                'status_flag':True,
                                'status': "success",
                                'error_details': None,
                                'data': serializer.data
                                }
                        return Response(data_response)
                return Response('try block executed')
        except Exception as error:
            return Response({
                'response_code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message':'username or password does not exist',
                'status_flag': False,
                'status': "success",
                'error_details': str(error),
                'data': []})


