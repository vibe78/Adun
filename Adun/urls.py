from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),  # Create a success view to redirect after form submission
    # path('subscribe/', views.subscribe, name='subscribe'),
    path('patient_reg/', views.patient_reg_view, name='patient_reg'),
    path('loginpage/', views.patient_login_view, name='loginpage'),
    path('profile/', views.profile, name ="profile"),
    path('staff_reg/', views.staff_reg_view, name ="staff_reg"),
    path('staff/', views.staff, name ="staff"),
    path('logout/', views.patient_logout_view, name='logout'),
    path('staff_logout/', views.staff_logout_view, name='staff_logout'),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('videocall/', views.videocall, name='videocall'),
    path('staff_login/', views.staff_login, name ="staff_login"),
    path('password_reset/', views.password_reset, name ="password_reset"),
    path('join_meeting/', views.join_meeting, name='join_meeting'),

    path('p_login_view/', views.p_login_view, name='p_login_view'),

    path('profilestudent/', views.profilestudent, name='profilestudent'),

    path('bookapointment_view/', views.bookapointment_view, name='bookapointment_view'),


    path('apointmentDetails_view/<id>/', views.apointmentDetails_view, name='apointmentDetails_view'),

    # other URL patterns for the app
]
    
