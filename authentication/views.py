import logging
from django.http import HttpResponseServerError, JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_maker, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *

from helper import format_dob, get_request_body, require_http_methods

from typing import *

if TYPE_CHECKING is True:
    from django.contrib.auth.models import AbstractUser

@require_http_methods(methods=['GET'])
def login(request):
    try:
        if request.user and request.user.is_authenticated:
            return HttpResponseRedirect("/curriculum/dashboard")
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
        _next:str = body.get('next', str())
        if request.user and request.user.is_authenticated:
            response_dict = {'status': True, 'message': "Login successful", 'next': _next}
        else:
            user:"Optional[AbstractUser]" = authenticate(request, username=username, password=password)
            if user is not None and not user.is_staff:
                login_maker(request, user)
                response_dict = {'status': True, 'message': "Login successful", 'next': _next}
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

@login_required
def logout_api(request):
    try:
        logout(request)
        response_dict = {
            'status': True,
            'message': 'Log out successfully',
            'login_url': '/accounts/login/'
        }
    
    except Exception as e:
        logging.error(e)
        logging.exception("authentication.views.logout_api")
        response_dict = {
            'status': False,
            'message': 'An error occurred while log out. Please try again later.',
            'login_url': '/accounts/login/'
        }
    
    return JsonResponse(response_dict)