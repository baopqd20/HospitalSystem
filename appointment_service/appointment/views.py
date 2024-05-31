from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from appointment.models import Appointment
from django.http import HttpResponse
import json, requests
# Create your views here.


def store_data(idPatient, idDoctor, date, idRoom, status, note, patientName, patientContact, doctorName, doctorContact, roomNumber, buildingName):
    data = Appointment(
        idPatient = idPatient,
        idDoctor = idDoctor,
        date = date,
        idRoom = idRoom,
        status = status,
        note = note,
        patientName = patientName,
        patientContact = patientContact,
        doctorName = doctorName,
        doctorContact = doctorContact,
        roomNumber = roomNumber,
        buildingName = buildingName,
    )

    data.save()
    return data


@csrf_exempt
def create_appointment(request):
    if request.method == 'POST':
        val1 = json.loads(request.body)
        idPatient = val1.get("Patient ID")
        idDoctor = val1.get("Doctor ID")
        date = val1.get("Date")
        idRoom = val1.get("Room ID")
        status = val1.get("Status")
        note = val1.get("Note")
        patientName = get_patient_name(idPatient)
        patientContact = get_patient_contact(idPatient)
        doctorName = get_doctor_name(idDoctor)
        doctorContact = get_doctor_contact(idDoctor)
        roomNumber = get_room_number(idRoom)
        buildingName = get_building_name(idRoom)

        resp = {}
        if val1 and idPatient and idDoctor and idRoom and status and note and patientName and patientContact and doctorName and doctorContact and roomNumber and buildingName:
            resdata = store_data(idPatient, idDoctor, date, idRoom, status, note, patientName, patientContact, doctorName, doctorContact, roomNumber, buildingName)
            if resdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Create Appointment Success'
                resp['data'] = {
                    'Appointment ID': resdata.id,
                }

            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Create Appointment Failed'

        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'All field are mandatory'
        
        return HttpResponse(json.dumps(resp), content_type='application/json')
    


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

def get_doctor_name(idDoctor):
    req = {}

    req["Doctor ID"] = idDoctor

    url = "http://127.0.0.1:3001/doctor-info/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    return val1['data']['Full Name']

def get_doctor_contact(idDoctor):
    req = {}

    req["Doctor ID"] = idDoctor

    url = "http://127.0.0.1:3001/doctor-info/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    return val1['data']['Contact']

def get_room_number(idRoom):
    req = {}

    req["Room ID"] = idRoom

    url = "http://127.0.0.1:4000/get-room/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    return val1['data']['Room Number']

def get_building_name(idRoom):
    req = {}

    req["Room ID"] = idRoom

    url = "http://127.0.0.1:4000/get-room/"
    datareq = json.dumps(req)
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data = datareq, headers = headers)
    val1 = json.loads(response.content.decode('utf-8'))

    return val1['data']['Building Name']