import json
import asyncio
from functools import wraps

from asgiref.sync import async_to_sync
from datetime import datetime
from typing import *

from django.http import HttpResponseNotAllowed
from django.utils.decorators import sync_and_async_middleware

T = TypeVar('T', bound=Callable)

def get_request_body(request) -> Union[List[Any], Dict[Any, Any]]:
    try:
        query_params = dict(request.GET.items())
        request_body = json.loads(request.body) if request.body else {}
        return {**query_params, **request_body}
    
    except:
        return {}

    

@sync_and_async_middleware
def require_http_methods(methods):
    def decorator(view: T) -> T:
        @wraps(view)
        async def async_inner(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return await view(request, *args, **kwargs)

        def sync_inner(request, *args, **kwargs):
            if request.method not in methods:
                return HttpResponseNotAllowed(methods)
            return view(request, *args, **kwargs)

        def inner(request, *args, **kwargs):
            if asyncio.iscoroutinefunction(view):
                return async_to_sync(async_inner)(request, *args, **kwargs)
            else:
                return sync_inner(request, *args, **kwargs)

        return inner

    return decorator

def format_dob(dob_str:str, format:str="%Y-%m-%d"):
    return datetime.strptime(dob_str, format).date()