import logging
from django.shortcuts import render
from django.http import JsonResponse

from helper import get_request_body

# Create your views here.

async def editor_index_page(request):
    return render(request, "editor/editor.html", {})

def execute_code(code):
    # Set up a namespace for the code to execute in
    namespace = {}
    # Execute the code in the namespace
    exec(code, namespace)
    # Capture the value of the last expression evaluated in the code
    result = namespace.get('__builtins__', {}).get('_')
    # Convert the result to a string and return it
    return str(result)


async def compile_the_code(request):
    response_dict = {'status': False, 'message': "Internal Server Down", 'output': ''}
    try:
        data = get_request_body(request)
        code = data.get('code', str())
        print ("code:", code)
        output = execute_code(str(code))
        response_dict = {'status': True, 'message': 'Success', 'output': output}

    except Exception as e:
        logging.error(e)
        logging.exception("editor.views.compile_the_code")

    return JsonResponse(response_dict)