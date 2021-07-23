from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User

#token manually
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.


class RegisterView(APIView):
    def post(self,request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']



        user = User(username=username,email=email)
        user.set_password(password)
        user.save()

        #token manually
        refresh = RefreshToken.for_user(user)

        return Response({'status':'Success',
                         'user_id':user.id,
                         'refresh': str(refresh),
                         'access': str(refresh.access_token),
    })
