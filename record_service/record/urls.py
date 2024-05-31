from django.urls import path
from . import views
urlpatterns = [
    path('create_record/',views.create_record,name='create_record'),
    path('search_record/',views.search_record,name='search_record')
]
