from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import *

'''This class registers the user'''
class RegisterView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def post(self, request):
        context = {}
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = serializer.save()
                # Log in the user immediately after successful registration
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return render(request, 'authentication/success.html',{'user':user})  
            except Exception as e:
                # Handle any errors that occur during user creation
                context["error"] = f"Error during user creation: {e}"
                return render(request, 'authentication/error.html', context)
        else:
            # If the serializer is not valid, render the signup page again with errors
            context['form'] = serializer.data
            context['errors'] = serializer.errors
            return render(request, 'authentication/signup.html', context)
        
    def get(self, request):
        return render(request, 'authentication/signup.html', {'form': {}})

'''This class login's the user'''
class LoginView(APIView):
    permission_classes = []
    authentication_classes = []
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return render(request, 'authentication/success.html',{'user':user})
            return render(request, 'authentication/signin.html', {'form': serializer.data, 'errors': 'Invalid credentials'})
        return render(request, 'authentication/signin.html', {'form': serializer.data, 'errors': serializer.errors})
        
        
    def get(self, request):
        return render(request, 'authentication/signin.html', {'form': {}})
    
'''This class logout's the user'''
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        logout(request)
        return redirect('login')