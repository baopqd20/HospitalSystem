from django.shortcuts import render
from .models import *
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


def store_data(fullName, address, cardId, gender, dob, contact):
    data = Patient(
        fullName = fullName,
        address = address,
        cardId = cardId,
        gender = gender,
        dob = dob,
        contact = contact
    )
    data.save()
    return data

@csrf_exempt
def create_patient(request):
    if request.method == 'POST':
        value = json.loads(request.body)
        fullName_data = value.get('fullName')
        address_data = value.get('address')
        cardId = value.get('cardId')
        gender = value.get('gender')
        dob = value.get('dob')
        contact = value.get('contact')

    if fullName_data:
        fullName = FullName(fname=fullName_data.get('first_name'), 
                            lname=fullName_data.get('last_name'))
        fullName.save()  
    else:
        fullName = None

    if address_data:
        address = Address(provice=address_data.get('provice'),
                          district=address_data.get('district'),
                          ward = address_data.get('ward'),
                          detail=address_data.get('detail'))
        address.save()
    else:
        address = None

    if fullName and address and cardId and gender and dob and contact:
        data = store_data(fullName, address, cardId, gender, dob, contact)
        resp = {}
        if data:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Comment complete.'
            resp['data'] = {
                'fullName': str(data.fullName)
            }
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Comment fail, Please try again.'
    return HttpResponse(json.dumps(resp),content_type='application/json')

def get_info_patient(id):
    patient = Patient.objects.filter(id=id).first()
    return patient

@csrf_exempt
def search_patient(request):
    if request.method == 'POST':
        value = json.loads(request.body)
        id = value.get('id')
        patient = get_info_patient(id)
        
        resp = {}
        if patient:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Comment complete.'
            resp['data'] = {
                'fullName': str(patient.fullName),
                'address': str(patient.address),
                'gender': patient.gender,
                'dob':str( patient.dob),
                'contact': patient.contact,

            }
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Comment fail, Please try again.'

    return HttpResponse(json.dumps(resp),content_type='application/json')
    

# def get_patient(id):
#     url = 'http://127.0.0.1:8888/patientInfo/'
#     d1 = {}
#     d1['id'] = id
#     data = json.dumps(d1)
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url,data=data,headers=headers)
#     value = json.loads(response.content.decode('utf-8'))
#     return value['data']
