import logging
from django.http import HttpResponseServerError, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_maker
from django.shortcuts import render
from .models import *

from helper import format_dob, get_request_body, require_http_methods

from typing import *

if TYPE_CHECKING is True:
    from django.contrib.auth.models import AbstractBaseUser

@require_http_methods(methods=['GET'])
async def login(request):
    try:
        return render(request, 'authentication/login.html', {})

    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        error_msg = (
            "<h1>some error occurred at the login page<br/>"
            f"Message: {str(e)}</h1>"
        )
        return HttpResponseServerError(error_msg)

@require_http_methods(methods=['POST'])    
def login_api(request):
    try:
        body = get_request_body(request)
        username:str = body['username']
        password:str = body['password']
        user:"Optional[AbstractBaseUser]" = authenticate(request, username=username, password=password)
        if user is not None:
            login_maker(request, user)
            response_dict = {'status': True, 'message': "Login successful"}
        else:
            response_dict = {'status': False, 'message': 'Invalid login credentials'}
    
    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        response_dict = {
            'status': False,
            'message': 'An error occurred while log in. Please try again later.',
            'categories': []
        }
    
    return JsonResponse(response_dict)

def signup(request):
    try:
        return render(request, 'authentication/signup.html', {})

    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        error_msg = (
            "<h1>some error occurred at the signup page<br/>"
            f"Message: {str(e)}</h1>"
        )
        return HttpResponseServerError(error_msg)

@require_http_methods(methods=['POST'])
async def signup_api(request):
    try:
        body = get_request_body(request)
        username = body['username']
        password = body['password']
        first_name = body['first_name'].strip()
        last_name = body['last_name'].strip()
        email_id = body['email_id'].strip()
        phone_number = body['phone_number'].strip()
        dateofbirth = body['dateofbirth'].strip()
        profile_picture = body.get('profile_picture', str())

        if authenticate(request, username, password):
            response_dict = {'status': False, 'message': 'Username already exists'}
        else:
            user:"User" = await User.objects.acreate(
                username=username,
                email=email_id,
                first_name=first_name,
                last_name=last_name,
            )
            user.set_password(password)

            Student.objects.acreate(
                phone_number=phone_number,
                dob = format_dob(dateofbirth),
                profile_picture=profile_picture,
                user=user
            )
            login_maker(request, user)

            response_dict = {'status': True, 'message': 'registration successfull.'}
    
    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        response_dict = {
            'status': False,
            'message': 'An error occurred while log in. Please try again later.',
            'categories': []
        }
    
    return JsonResponse(response_dict)