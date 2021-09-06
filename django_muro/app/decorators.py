from django.shortcuts import redirect
from datetime import datetime, time, timedelta


def login_required(function):

    def wrapper(request, *args):
        if 'user' not in request.session:
            return redirect('/login')
        resp = function(request, *args)
        return resp
    
    return wrapper


