from functools import wraps
from django.shortcuts import redirect

class unlock_required(object):

    def __init__(self, view_func):
        self.view_func = view_func
        wraps(view_func)(self)

    def __call__(self, request, *args, **kwargs):
        if 'en_key' not in request.session:
            return redirect('unlock')

        return  self.view_func(request, *args, **kwargs)