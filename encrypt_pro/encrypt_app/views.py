import hashlib,os
from . import models,serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


class Usersignup(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        try:
                serializer = serializers.UserSerializer(data=request.data)
                if serializer.is_valid():
                    salt = os.urandom(16)
                    pswd = request.data['password'].encode('utf-8')
                    serializer.validated_data['password'] = hashlib.blake2s(salt+pswd).hexdigest()
                    serializer.validated_data['salt'] = salt.hex()
                    serializer.save()
                return Response({'response_code': status.HTTP_200_OK,
                                 'message': "Registered successfully",
                                 'status_flag': True,
                                 'status': "success",
                                 'error_details': None,

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
                # salt = bytes.fromhex(user.salt)
                # pwd = request.data['password'].encode('utf-8')
                password = hashlib.blake2s(bytes.fromhex(user.salt)+request.data['password'].encode('utf-8')).hexdigest()
                if password == user.password:
                    data_response = {
                            'response_code': status.HTTP_200_OK,
                            'message': "logged in successfully",
                            'status_flag':True,
                            'status': "success",
                            'error_details': None,
                            'data': serializer.data
                            }
                    return Response(data_response)
            return Response('wrong credentials')
        except Exception as error:
            return Response({
                'response_code':status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message':'username or password does not exist',
                'status_flag': False,
                'status': "success",
                'error_details': str(error),
                'data': []})







