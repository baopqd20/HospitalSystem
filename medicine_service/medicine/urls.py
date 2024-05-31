from django.urls import path
from . import views
urlpatterns = [
    path('info_medicine/',views.search_medicine, name='info_medicine')
]
