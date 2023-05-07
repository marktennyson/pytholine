import logging, time
from django.utils import timezone
from django.http import JsonResponse, HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render
from django.db.models import (
    F, Subquery, Sum, Window, Case, When, IntegerField,
    OuterRef, Value, 
    CharField, Count
    )
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat, Coalesce
from django.db.models.expressions import OrderBy
from authentication.models import Student
from helper import get_request_body, require_http_methods, execute_code
from .models import (
    QuestionCategory,
    Question, StudentAnswer,
    Batch
)
from typing import *

# Create your views here.

@require_http_methods(methods=["GET"])
def list_all_batches_by_student(request):
    try:
        body = get_request_body(request)
        student_id:int = int(body['student_id'])
        # print ("test:", QuestionCategory.objects.filter(batch__id=))
        batches = Batch.objects.filter(student__id=student_id).annotate(
            category_ids=Subquery(QuestionCategory.objects.filter(batch__id=F('pk')).values_list('pk', flat=True)),
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
        first_question_uuid_query = Subquery(Question.objects.filter(category=OuterRef('pk')).order_by('id').values('uuid')[:1], output_field=CharField())
        
        categories = QuestionCategory.objects.filter(is_active=True).annotate(
            total_score=Coalesce(Sum('question__marks'), 0.0),
            student_score=Value("-"),
            last_submission_date=Value("-"),
            no_of_question=Count('question'),
            first_question_uuid=first_question_uuid_query
        ).values(
            'pk', 'name', 'description', 'no_of_question', 'total_score', 
            'student_score', 'last_submission_date', 'first_question_uuid'
        )

        response_dict = {
            'status': True,
            'message': 'Successfully retrieved all categories',
            'categories': list(categories)
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

@login_required    
def dashboard(request):
    try:
        return render(request, "curriculum/dashboard.html", {'llist':list(range(10))})
    
    except Exception as e:
        logging.error(e, exc_info=True)
        logging.exception("curriculum.views.list_all_categories")
        error_msg = (
            "<h1>some error occurred at dashboard<br/>"
            f"Message: {str(e)}</h1>"
        )
        return HttpResponseServerError(error_msg)
    

def editor_index_page(request):
    return render(request, "editor/editor.html", {})


def compile_the_code(request):
    time_s1 = time.time()
    response_dict = {'status': False, 'message': "Internal Server Down", 'output': ''}
    try:
        data = get_request_body(request)
        code = data.get('code', str())
        output, is_error = execute_code(str(code))
        message = "Success"
        is_execution_succeed = True
        is_correct_ans = False

        if is_error is True:
            message = "error occured at the time of execution."
            is_execution_succeed = False
            output = output.split("\n")[-1]
        if not output:
            output = message = "Output not found. You probably missed print or return keywords."
            is_execution_succeed = False

        time_s2 = time.time()

        response_dict = {
            'status': True, 'is_execution_succeed': is_execution_succeed,
            'output': output, 'time_taken': round((time_s2-time_s1), 2), 
            'time_taken_unit': 'second', 'message': message,
            'is_correct_answer': is_correct_ans
            }

    except Exception as e:
        logging.error(e)
        logging.exception("curriculum.views.compile_the_code")

    return JsonResponse(response_dict)

@login_required
def show_question_page(request, uuid):
    try:
        question:Optional[Question] = Question.objects.filter(uuid=uuid).first()

        next_question_url:str = f"/curriculum/question/{question.next.uuid}" if question.next else ""
        priv_question_url:str = f"/curriculum/question/{question.previous.uuid}" if question.previous else ""

        context:Dict[str, Any] = {
            'question': question,
            'next_question_url': next_question_url,
            'priv_question_url': priv_question_url
        }

        if question is None:
            return HttpResponseNotFound() 
        return render(request, "curriculum/question.html", context=context)
    
    except Exception as e:
        logging.error(e)
        logging.exception("curriculum.views.show_question_page")
        error_msg = (
            "<h1>some error occurred at dashboard<br/>"
            f"Message: {str(e)}</h1>"
        )
        return HttpResponseServerError(error_msg)

@login_required
def submit_answer(request):
    try:
        qd = get_request_body(request)
        question_id:int = int(qd['question_id'])
        student_id:int = int(qd['student_id'])
        body:str = str(qd['body'])
        _answer:str = str(qd['answer'])
    
        answer:"StudentAnswer"
        answer, _ = StudentAnswer.objects.get_or_create(
            student_id=student_id,
            question_id=question_id,
        )

        if answer.question.correct_answer.strip() == _answer.strip():
            answer.is_correct = True
            answer.score = answer.question.marks

        answer.answer = _answer
        answer.body = body
        answer.last_modified_at = timezone.now()
        answer.save()

        response_dict = {
            'status': True,
            'message': "Answer submitted successfully"
        }
    
    except Exception as e:
        logging.error(e)
        logging.exception("curriculum.views.submit_answer")

        response_dict = {
            'status': False,
            'message': 'An error occurred while submitting the answer. Please try again later.',
        }
    
    return JsonResponse(response_dict)