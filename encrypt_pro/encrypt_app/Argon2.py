from argon2 import PasswordHasher
from . import models,serializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
import codecs,uuid

class Usersignup(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
        try:
                serializer = serializers.UserSerializer(data=request.data)
                if serializer.is_valid():
                    # argon2Hasher = PasswordHasher(
                    #     time_cost=2,
                    #     memory_cost=64,
                    #     parallelism=1,
                    #     hash_len=16,
                    #     salt_len=16,
                    #
                    # )
                    hash = PasswordHasher.hash(request.data['password'])
                    serializer.validated_data['password'] = hash
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
                serializer1 = serializers.UserSerializer(instance=user)
                # if PasswordHasher.verify(user.password,serializer.validated_data['password']):
                if user:
                    argon2Hasher = PasswordHasher(
                        time_cost=2,
                        memory_cost=64,
                        parallelism=1,
                        hash_len=16,
                        salt_len=16,

                    )
                    # hash = argon2Hasher.hash(request.data['password'])
                    if argon2Hasher.verify(user.password,serializer.validated_data['password']):
                        data_response = {
                                'response_code': status.HTTP_200_OK,
                                'message': "logged in succesfully",
                                'status_flag':True,
                                'status': "success",
                                'error_details': None,
                                'data': serializer1.data
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



# in built salting is used in argon2 algorithm
# no need separate column in database
#we can set parallelism,salt length,rounds,time_cost,memory_cost etc..

