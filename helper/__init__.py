import json
from functools import wraps
from typing import Callable, TypeVar

from django.http import HttpResponseNotAllowed
from django.utils.decorators import sync_and_async_middleware

T = TypeVar('T', bound=Callable)

def get_request_body(request):
    try:
        return json.loads(request.body)
    except:
        return {}
    

@sync_and_async_middleware
def require_http_methods(methods):
    def decorator(view: T) -> T:
        @wraps(view)
        async def inner(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return await view(request, *args, **kwargs)

        def sync_inner(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return view(request, *args, **kwargs)

        if hasattr(view, 'async_view') and view.async_view:
            return inner
        else:
            return sync_inner

    return decorator