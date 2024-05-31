from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Doctor, Fullname, Address, Department
import json

# Create your views here.


def store_data(fullname, gender, address, cardId, dob, department, email):
    data = Doctor(
        fullname=fullname,
        gender=gender,
        address=address,
        cardId=cardId,
        dob=dob,
        department=department,
        email=email
    )
    data.save()
    return data

def get_doctor(id):
     doctor = Doctor.objects.filter(id = id). first()
     return doctor

@csrf_exempt
def create_doctor(request):
    if request.method == 'POST':
        val1 = json.loads(request.body)
        fullname_data = val1.get("Full Name")
        gender = val1.get("Gender")
        address_data = val1.get("Address")
        cardId = val1.get("Card Id")
        dob = val1.get("Date of birth")
        department_data = val1.get("Department")
        email = val1.get("Email")

        if fullname_data:
            fullname = Fullname(fname = fullname_data.get('First Name'), 
                                lname = fullname_data.get('Last Name')
                                )
            fullname.save()
        
        if address_data:
             address = Address(provice = address_data.get('Provice'),
                                district = address_data.get("District"),
                                ward = address_data.get("Ward"),
                                details = address_data.get("Details"))
             address.save()


        if department_data:
             department = Department(name = department_data.get('Name'),
                                     specialization = department_data.get('Specialization'),
                                     departmentId = department_data.get('Department ID'),
                                     description = department_data.get('Description'))
             department.save()
        resp = {}

        if fullname and gender and address and cardId and dob and department and email:
            data = store_data(fullname, gender, address, cardId, dob, department, email)

            if data:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Create Doctor Complete'
                resp['data'] = {
                     'Fullname': str(data.fullname),
                     'Address': str(data.address)
                }
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Create Doctor Failed'
    else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'All fields are mandatory'

    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def search_doctor(request):
    resp = {}
    if request.method == 'POST':
        val1 = json.loads(request.body)
        id = val1.get("Doctor ID")
        doctor = get_doctor(id)

        if doctor:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'Full Name': str(doctor.fullname),
                'Contact': doctor.email
            }
        else:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Room not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')