from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from user_model.models import UserRegistration

# Function to fetch user data.
def user_data(uname):
    user = UserRegistration.objects.filter(email=uname).first()
    return user


@csrf_exempt
def user_info(request):
    resp = {}
    
    if request.method == 'POST':
        if 'application/json' in request.META.get('CONTENT_TYPE', ''):
            val1 = json.loads(request.body)
            uname = val1.get('User Name')
            if uname:
                # Call function to get user info.
                user = user_data(uname)
                if user:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = {
                        'First Name': user.fname,
                        'Last Name': user.lname,
                        'Mobile Number': user.mobile,
                        'Email Id': user.email,
                        'Address': user.address
                    }
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields are mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'

    return HttpResponse(json.dumps(resp), content_type='application/json')


def user_data_2(lname):
    user = UserRegistration.objects.filter(lname=lname).first()
    return user
# Function to handle user info request.
@csrf_exempt
def user_info_2(request):
    resp = {}
    
    if request.method == 'POST':
        if 'application/json' in request.META.get('CONTENT_TYPE', ''):
            val1 = json.loads(request.body)
            lname = val1.get('User Name')
            if lname:
                # Call function to get user info.
                user = user_data_2(lname)
                if user:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = {
                        'First Name': user.fname,
                        'Last Name': user.lname,
                        'Mobile Number': user.mobile,
                        'Email Id': user.email,
                        'Address': user.address
                    }
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields are mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'

    return HttpResponse(json.dumps(resp), content_type='application/json')