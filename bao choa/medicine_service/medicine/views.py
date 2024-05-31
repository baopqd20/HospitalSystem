from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse

# Create your views here.
def get_info_medicine(name):

    info_medicine = Medicine.objects.filter(name=name).first()
    return info_medicine

@csrf_exempt
def search_medicine(request):
    if request.method == 'POST':
        value = json.loads(request.body)
        name = value.get('name')
        medicine = get_info_medicine(name)

        resp = {}
        if medicine:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Comment complete.'
            resp['data'] = {
                'name': medicine.name,
                'price': medicine.price,
                'brand': medicine.brand,
                'expDate':str( medicine.expdate),
                'note': medicine.note,
                'status': medicine.status,
            }
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Comment fail, Please try again.'

    return HttpResponse(json.dumps(resp),content_type='application/json')