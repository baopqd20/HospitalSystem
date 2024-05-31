from django.shortcuts import render
from .models import *
import json
import requests
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
# Create your views here.

def cal_age(dob_str):
    birthdate = datetime.strptime(dob_str,"%Y-%m-%d")
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def get_patient_name(id):
    urlPatient = 'http://192.168.0.103:3000/search_patient/'
    inputP = {}
    inputP["id"] = id
    dataP = json.dumps(inputP)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(urlPatient,data=dataP,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['fullName']

def get_patient_contact(id):
    urlPatient = 'http://192.168.0.103:3000/search_patient/'
    inputP = {}
    inputP["id"] = id
    dataP = json.dumps(inputP)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(urlPatient,data=dataP,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['contact']

def get_patient_dob(id):
    urlPatient = 'http://192.168.0.103:3000/search_patient/'
    inputP = {}
    inputP["id"] = id
    dataP = json.dumps(inputP)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(urlPatient,data=dataP,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['dob']


def get_doctor_name(id):
    urlDoctor = 'http://192.168.0.101:3001/doctor-info/'
    inputD = {}
    inputD['Doctor ID'] = id
    dataD = json.dumps(inputD)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(urlDoctor,data=dataD,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Full Name']

def get_doctor_contact(id):
    urlDoctor = 'http://192.168.0.101:3001/doctor-info/'
    inputD = {}
    inputD['Doctor ID'] = id
    dataD = json.dumps(inputD)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(urlDoctor,data=dataD,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Contact']

def store_record(idPatient,idDoctor,result,medicine,boarding,note,reSchedule,fee,patientName,patientContact,age,doctorName,doctorContact):
    data = Record(
        idPatient=idPatient,
        idDoctor=idDoctor,
        result=result,
        medicine=medicine,
        boarding=boarding,
        note=note,
        reSchedule=reSchedule,
        fee=fee,
        patientName=patientName,
        patientContact=patientContact,
        age=age,
        doctorName=doctorName,
        doctorContact =doctorContact
    )
    data.save()
    return data
@csrf_exempt
def create_record(request):
    
    if request.method == 'POST':
        value = json.loads(request.body)
        idPatient = value.get('idPatient')
        idDoctor = value.get('idDoctor')
        result = value.get('result')
        medicine = value.get('medicine')
        boarding = value.get('boarding')
        note = value.get('note')
        reSchedule = value.get('reSchedule')
        fee = value.get('fee')
        patientName = get_patient_name(idPatient)
        patientContact = get_patient_contact(idPatient)
        dobP = get_patient_dob(idPatient)
        age = cal_age(dobP)
        doctorName = get_doctor_name(idDoctor)
        doctorContact = get_doctor_contact(idDoctor)
        print(idPatient,idDoctor,result,medicine,boarding,note,reSchedule,fee,patientName,patientContact,age,doctorName,doctorContact)
        resp = {}
        if idPatient and idDoctor and result and medicine and note and reSchedule and fee and patientName and patientContact and age and doctorName and doctorContact:
            data = store_record(idPatient,idDoctor,result,medicine,boarding,note,reSchedule,fee,patientName,patientContact,age,doctorName,doctorContact)
            if data:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Comment complete.'
                resp['data'] = {
                    'patientName': data.patientName,
                    'patientDoctor': data.doctorName,
                    'result': data.result,
                    'note': data.note
                }
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Comment fail, Please try again.'

    return HttpResponse(json.dumps(resp),content_type='application/json')

# medicine, fee, bedFee, 
def get_info_record(id):
    record = Record.objects.filter(id=id).first()
    return record

def get_fee_bed(idBed):
    urlBed = 'http://192.168.0.101:4000/get-bed/'
    inputB = {}
    inputB['Bed ID'] = idBed
    dataD = json.dumps(inputB)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(urlBed,data=dataD,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['price']

@csrf_exempt
def search_record(request):
    if request.method == 'POST':
        value = json.loads(request.body)
        id = value.get('id')
        record = get_info_record(id)
        if record.boarding:
            bedFee = get_fee_bed(record.boarding)
        else:
            bedFee = "0"

        resp = {}
        if record:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Comment complete.'
            resp['data'] = {
                "medicine": record.medicine,
                "fee": str(record.fee),
                "bedFee": bedFee,
                'idPatient': str(record.idPatient)
            }
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Comment fail, Please try again.'
    return HttpResponse(json.dumps(resp),content_type='application/json')

    