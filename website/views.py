import logging
from django.http import HttpResponseServerError
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def question_listing(request):
    try:
        return render(request, "website/question_listing.html", {})
    
    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        error_msg = (
            "<h1>some error occurred at the question listing page<br/>"
            f"Message: {str(e)}</h1>"
        )
        return HttpResponseServerError(error_msg)

@login_required    
def dashboard(request):
    try:
        return render(request, "website/dashboard.html", {'llist':list(range(10))})
    
    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        error_msg = (
            "<h1>some error occurred at the batch listing page<br/>"
            f"Message: {str(e)}</h1>"
        )
        return HttpResponseServerError(error_msg)