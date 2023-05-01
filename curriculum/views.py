import logging
from django.http import JsonResponse
from helper import require_http_methods
from .models import (
    QuestionCategory,
    Question,
)
from typing import *

# Create your views here.

@require_http_methods(methods=["GET"])
def list_all_categories(request):
    try:
        categories:List[Dict[str, Any]] = list(QuestionCategory.objects.filter(
            is_active=True).values('pk', 'name', 'description'))

        response_dict = {
            'status': True,
            'message': 'Successfully retrieved all categories',
            'categories': categories
        }

    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        response_dict = {
            'status': False,
            'message': 'An error occurred while retrieving the categories. Please try again later.',
            'categories': []
        }

    return JsonResponse(response_dict)
