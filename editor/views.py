import logging
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

async def editor_index_page(request):
    return render(request, "editor/editor.html", {})

async def execute_code(code):
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
        print ("request.POST:", request.body)
        code = request.POST
        # output = execute_code(code)
        # response_dict = {'status': True, 'message': 'Success', 'output': await output}

    except Exception as e:
        logging.error(e)
        logging.exception("editor.views.compile_the_code")

    return JsonResponse(response_dict)