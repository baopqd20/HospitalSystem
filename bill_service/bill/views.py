from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
import requests

# Create your views here.

def store_bill(idPayment,idEmployee,recipientName,medicine,fee,bedFee,paymentDay,contact,total):
    data = Bill(
        idPayment=idPayment,
        idEmployee=idEmployee,
        recipientName=recipientName,
        medicine=medicine,
        fee=fee,
        bedFee=bedFee,
        paymentDay=paymentDay,
        contact=contact,
        total=total
    )
    data.save()
    return data

def get_info_payment_medicine(id):
    url = 'http://192.168.0.101:5001/payment-complete/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Medicine List']

def get_info_payment_fee(id):
    url = 'http://192.168.0.101:5001/payment-complete/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Fee']

def get_info_payment_bedFee(id):
    url = 'http://192.168.0.101:5001/payment-complete/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Bed Fee']

def get_info_payment_paymentDay(id):
    url = 'http://192.168.0.101:5001/payment-complete/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Payment Date']

def get_info_payment_contact(id):
    url = 'http://192.168.0.101:5001/payment-complete/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Contact']


def get_info_payment_total(id):
    url = 'http://192.168.0.101:5001/payment-complete/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    value = json.loads(res.content.decode('utf-8'))
    return value['data']['Total']


def call_api_success(id):
    url = 'http://192.168.0.101:5001/payment-update/'
    input = {}
    input['Payment ID'] = id
    data = json.dumps(input)
    headers = {'Content-Type':'application/json'}
    res = requests.post(url,data=data,headers=headers)
    return 1

@csrf_exempt
def create_bill(request):
    if request.method == 'POST':
        value = json.loads(request.body)
        idPayment = value.get('idPayment')
        idEmployee = value.get('idEmployee')
        recipientName = value.get('recipientName')

        medicine = get_info_payment_medicine(idPayment)
        fee = get_info_payment_fee(idPayment)
        bedFee = get_info_payment_bedFee(idPayment)
        paymentDay = get_info_payment_paymentDay(idPayment)
        contact = get_info_payment_contact(idPayment)
        total = get_info_payment_total(idPayment)

        print()

        if idPayment and idEmployee and recipientName and fee and bedFee and paymentDay and contact and total:
            data = store_bill(idPayment,idEmployee,recipientName,medicine,fee,bedFee,paymentDay,contact,total)

            resp = {}
            if data:
                call_api_success(idPayment)
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Comment complete.'
                resp['data'] = {
                    'idPayment': data.idPayment,
                    'idEmployee': data.idEmployee,
                    'recipientName': data.recipientName,
                    'medicine': data.medicine,
                    'fee': str(data.fee),
                    'bedFee': str(data.bedFee),
                    'paymentDay': str(data.paymentDay),
                    'contact': data.contact,
                    'total': data.total 
                }
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Comment fail, Please try again.'

    return HttpResponse(json.dumps(resp),content_type='application/json')

