from django.shortcuts import render
from roombed.models import Room, Bed
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

def get_room(id):
    room = Room.objects.filter(id = id).first()
    return room

def get_bed(id):
    bed = Bed.objects.filter(id = id).first()
    return bed


@csrf_exempt
def search_room(request):
    resp = {}
    if request.method == 'POST':
        val1 = json.loads(request.body)
        id = val1.get("Room ID")
        room = get_room(id)

        if room:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'Floor': room.floor,
                'Note': room.note,
                'Type': room.type,
                'Building Name': room.buildingName,
                'Room Number': room.roomNumber
            }
        else:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Doctor not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')


@csrf_exempt
def search_bed(request):
    resp = {}
    if request.method == 'POST':
        val1 = json.loads(request.body)
        id = val1.get("Bed ID")
        bed = get_bed(id)

        if bed:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['data'] = {
                'room': str(bed.room),
                'note': bed.note,
                'price': bed.price,
                'Bed Number': bed.bedNumber
            }
        else:
            resp['status'] = 'Success'
            resp['status_code'] = '200'
            resp['message'] = 'Room not found'
    return HttpResponse(json.dumps(resp), content_type='application/json')
