from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from payment.models import Payment
import json
from django.http import HttpResponse
import requests
# Create your views here.
def store_data(idRecord, patientName, total, medicine, fee, status, contact, idPatient, bedfee):
    data = Payment(
        idRecord = idRecord,
        patientName = patientName,
        total = total,
        medicine = medicine,
        fee = fee,
        status = status,
        contact = contact,
        idPatient = idPatient,
        bedFee = bedfee
    )

    data.save()
    return data

def get_data(id):
    payment = Payment.objects.filter(id = id).first()
    return payment


def update_data(id):
    payment = Payment.objects.filter(id = id).first()
    if payment:
        payment.status = 'Success'
        payment.save()
    return payment


@csrf_exempt
def create_payment(request):
    if request.method =='POST':
        val1 = json.loads(request.body)

        idRecord = val1.get("Record ID")
        status = val1.get("Status")
        
        medicine = get_medicine_list(idRecord)
        idPatient = get_id_patient(idRecord)
        fee = get_fee(idRecord)
        bedfee = get_bed_fee(idRecord)
        total = int(get_medicine_total(idRecord)) + int(fee) + int(bedfee)
        patientName = get_patient_name(idPatient)
        contact = get_patient_contact(idPatient)
     
        resp = {}

        if val1 and idRecord and status:
            resdata = store_data(idRecord, patientName, total, medicine, fee, status, contact, idPatient, bedfee)

            if resdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Create Payment Success'

            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Create Payment Failed'

        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'All field are mandatory'
        
        return HttpResponse(json.dumps(resp), content_type='application/json')
    

def get_medicine_list(idRecord):

    req = {}
    req["id"] = idRecord

    url = "http://192.168.0.103:7000/search_record/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    medicine_list = val1['data']['medicine'].split(',')

    medicineStr = ''
    for medicine in medicine_list:
        medicineStr = medicineStr + medicine + ":" + str(get_medicine_price(medicine)) + " "

    return medicineStr

def get_medicine_total(idRecord):

    req = {}
    req["id"] = idRecord

    url = "http://192.168.0.103:7000/search_record/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    medicine_list = val1['data']['medicine'].split(',')

    medicine_total = 0
    for medicine in medicine_list:
        if get_medicine_price(medicine) != "het hang":
            medicine_total = medicine_total + int(get_medicine_price(medicine))
    
    return medicine_total
def get_medicine_price(medicineName):

    req = {}
    req["name"] = medicineName

    url = "http://192.168.0.103:4001/info_medicine/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))
    if val1['data']['status'] == "con hang":
        return val1['data']['price']

    return val1['data']['status']



def get_id_patient(idRecord):
    req = {}
    req["id"] = idRecord

    url = "http://192.168.0.103:7000/search_record/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return val1['data']['idPatient']

def get_fee(idRecord):
    req = {}
    req["id"] = idRecord

    url = "http://192.168.0.103:7000/search_record/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return val1['data']['fee']

def get_bed_fee(idRecord):
    req = {}
    req["id"] = idRecord

    url = "http://192.168.0.103:7000/search_record/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))
    return val1['data']['bedFee']


def get_patient_name(idPatient):
    req = {}

    req["id"] = idPatient

    url = "http://192.168.0.103:3000/search_patient/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    return val1['data']['fullName']
    # return "Pham Quoc Bao"

def get_patient_contact(idPatient):
    req = {}
    req["id"] = idPatient
    url = "http://192.168.0.103:3000/search_patient/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    return val1['data']['contact']
    # return "0123456789"


@csrf_exempt
def complete_payment(request):
    if request.method == 'POST':
        val1 = json.loads(request.body)
        id = val1.get("Payment ID")
        payment = get_data(id)
        resp = {}
        if payment:
            resp['status'] = 'Success',
            resp['status_code'] = '200',
            resp['message'] = 'Payment Complete'
            resp['data'] = {
                "Medicine List": payment.medicine,
                "Fee": payment.fee,
                "Bed Fee": payment.bedFee,
                "Payment Date": str(payment.createdDate),
                "Contact": payment.contact,
                "Total": payment.total
            }
        else:
            resp['status'] = 'Failed',
            resp['status_code'] = '400',
            resp['message'] = 'Payment Failed'
            resp['data'] = 'Payment ID not correct'
    else:
        resp['status'] = 'Failed',
        resp['status_code'] = '400',
        resp['message'] = 'All Fields are Mandatory'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def update_payment(request):
    if request.method == 'POST':
        val1 = json.loads(request.body)
        id = val1.get("Payment ID")
        payment = update_data(id)
        resp = {}
        if payment:
            resp['status'] = 'Success',
            resp['status_code'] = '200',
            resp['message'] = 'Update Payment Complete'
        else:
            resp['status'] = 'Failed',
            resp['status_code'] = '400',
            resp['message'] = 'Payment Failed'
            resp['data'] = 'Update Payment Failed'
    else:
        resp['status'] = 'Failed',
        resp['status_code'] = '400',
        resp['message'] = 'All Fields are Mandatory'
    return HttpResponse(json.dumps(resp), content_type='application/json')
