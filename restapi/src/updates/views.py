import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from django.views.generic import View

from .models import Update

def json_example_view(request):
    """
    URI -- for a REST API
    """
    data = {
        "count": 1000,
        "content": "Some new content"
    }
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
    #return JsonResponse(data)

class JSONCBV(View):
    def get(self, request, *args, **kwargs):
        data = {
            "count": 1000,
            "content": "Some new content"
        }

        return JsonResponse(data)


class JsonResponseMixin(object):
    def render_to_json_response(self, context, **response_kwargs):
        return JsonResponse(self.get_data(context), **response_kwargs)

    def get_data(self, context):
        return context
