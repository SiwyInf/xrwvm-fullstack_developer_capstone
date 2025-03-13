from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt

# Get an instance of a logger
logger = logging.getLogger(__name__)

@csrf_exempt
def login_user(request):
    try:
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=400)
    except KeyError as e:
        return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)

@csrf_exempt
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"message": "User successfully logged out."})
    else:
        return JsonResponse({"error": "No user was logged in."}, status=400)

@csrf_exempt
def registration(request):
    try:
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data['firstName']
        last_name = data['lastName']
        email = data['email']
        
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username already exists"}, status=400)

        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already exists"}, status=400)

        # Create a new user
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        
        # Automatically log in the newly registered user
        login(request, user)
        
        return JsonResponse({"userName": username, "status": "Authenticated"})
    except KeyError as e:
        return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
    except Exception as e:
        logger.error(f"Error during registration: {str(e)}")
        return JsonResponse({"error": "Something went wrong during registration."}, status=500)
