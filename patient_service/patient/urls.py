from django.urls import path
from . import views

urlpatterns = [
    path('create_patient/',views.create_patient,name='create_patient'),
    path('search_patient/',views.search_patient, name='search_patient'),
]
