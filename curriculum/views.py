import logging
from django.http import JsonResponse
from django.db.models import (
    F, Subquery, 
    OuterRef, Value, 
    CharField
    )
from django.db.models.functions import Concat
from authentication.models import Student
from helper import get_request_body, require_http_methods
from .models import (
    QuestionCategory,
    Question,
    Batch
)
from typing import *

# Create your views here.

@require_http_methods(methods=["GET"])
def list_all_batches_by_student(request):
    try:
        body = get_request_body(request)
        student_id:int = int(body['student_id'])

        batches = Batch.objects.filter(student__id=student_id).annotate(
            category_ids=Subquery(QuestionCategory.objects.filter(batch__id=OuterRef('id')).values_list('id', flat=True)),
            language_name=F('language__name'),
            language_logo=Concat(Value("/static/images/"), F('language__logo'), Value("/"), output_field=CharField()),
            ).values('pk', 'name', 'language_name', 'category_ids', 'start_date', 'end_date', 'language_logo')

        
        response_dict = {'status': True, 'message': 'Success', 'batches': list(batches)}
    
    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_batches_by_student")
        response_dict = {
            'status': False,
            'message': 'An error occurred while retrieving the batches. Please try again later.',
            'categories': []
        }
    
    return JsonResponse(response_dict)

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
