import logging
import subprocess
from django.shortcuts import render
from django.http import JsonResponse
import time

from helper import get_request_body

from typing import *

# Create your views here.

async def editor_index_page(request):
    return render(request, "editor/editor.html", {})

def execute_code(code) -> Tuple[str, bool]:
    is_error:bool = False
    try:
        result:str = subprocess.check_output(['python3.10', '-c', code], stderr=subprocess.STDOUT).decode('utf-8').strip()
    except subprocess.CalledProcessError as e:
        is_error = True
        result = e.output.decode('utf-8').strip()

    return str(result), is_error


async def compile_the_code(request):
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
        logging.exception("editor.views.compile_the_code")

    return JsonResponse(response_dict)