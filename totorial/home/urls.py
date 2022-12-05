from django.urls import path,include
from .import views

urlpatterns = [

    path('', views.index,name='home'),
    path('About/', views.about, name='about'),
    path('Booking/', views.booking ,name='booking'),

    path('Doctors/', views.doctors,name='doctors'),

    path('Contact/', views.contact,name='contact'),

    path('Department/',views.department,name='department')
]
