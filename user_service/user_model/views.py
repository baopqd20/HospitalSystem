from __future__ import unicode_literals
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import UserRegistration

def data_insert(fname, lname, email, mobile, password, address):
    user_data = UserRegistration(
        fname=fname,
        lname=lname,
        email=email,
        mobile=mobile,
        password=password,
        address=address
    )
    user_data.save()
    return 1

@csrf_exempt
def registration_req(request):
    if request.method == 'POST':
        val1 = json.loads(request.body)
        fname = val1.get("First Name")
        lname = val1.get("Last Name")
        email = val1.get("Email Id")
        mobile = val1.get("Mobile Number")
        password = val1.get("Password")
        cnf_password = val1.get("Confirm Password")
        address = val1.get("Address")
        
        resp = {}
        
        if fname and lname and email and mobile and password and cnf_password and address:
            if len(str(mobile)) == 10:
                if password == cnf_password:
                    respdata = data_insert(fname, lname, email, mobile, password, address)
                    if respdata:
                        resp['status'] = 'Success'
                        resp['status_code'] = '200'
                        resp['message'] = 'User is registered successfully.'
                    else:
                        resp['status'] = 'Failed'
                        resp['status_code'] = '400'
                        resp['message'] = 'Unable to register user. Please try again.'
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'Password and Confirm Password should be same.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Mobile Number should be 10 digits.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'All fields are mandatory.'
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Invalid request method.'
    
    return HttpResponse(json.dumps(resp), content_type='application/json')
