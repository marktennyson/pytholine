import logging
from django.http import HttpResponseServerError
from django.shortcuts import render

# Create your views here.

def login(request):
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