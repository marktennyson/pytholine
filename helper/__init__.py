import json

def get_request_body(request):
    try:
        return json.loads(request.body)
    except:
        return {}