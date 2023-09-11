from django.shortcuts import render, redirect, HttpResponse
from .forms import *
from .models import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import StaffRegistration
from .forms import StaffRegistrationForm  # Make sure to import your form

from django.http import JsonResponse, HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect

from django.urls import reverse
from django.utils.timezone import now
# from .forms import PatientRegistrationForm, PatientLoginForm



def index(request):
    obj = CarouselItem.objects.all()
    about_content = AboutContent.objects.first()  
    opening_hours = OpeningHours.objects.all()
    appointments = Appoint_contact.objects.all()
    home_content = ApointmentContent.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    team_members = TeamMember.objects.all()
    
    
    context = {
        'obj': obj,
        'about_content': about_content,
        'opening_hours': opening_hours,
        'appointments': appointments,
        'home_content': home_content,
        'services': services,
        'testimonials': testimonials,
        'team_members': team_members 
    }
    return render(request, 'index.html', context)
    

def about(request):
    about_content = AboutContent.objects.first()  
   
    context = {
        'about_content': about_content,

    }
    return render(request, 'about.html', context)


def appointment(request):
    #appointment = appointment.object.all()
    context={}
    return render(request, 'appointment.html', context )

def success():
    return  HttpResponse("thank...! You will get a feedback from you soon")



def service(request):
    services = Service.objects.all()
    appointments = Appoint_contact.objects.all()
   
    context = {
        'services': services,
        'appointments': appointments
    }
    return render(request, 'service.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Service

# View function for the first item
# def service(request, service_id):
#     services = get_object_or_404(Service, id=service_id)
#     return render(request, 'service.html', {'services': services})

# View function for the second item
# def another_service_detail(request, service_id):
#     service = get_object_or_404(Service, id=service_id)
#     return render(request, 'another_service_detail.html', {'service': service})



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index') 
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def patient_reg_view(request):
    if request.method == 'POST':
        #matric_num = request.POST['matric_num']
        first_name = request.POST['first_name']
        last_name  = request.POST['first_name']
        password  = request.POST['password']
        comfirm_password = request.POST['comfirm_password']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        maritalstat = request.POST['maritalstat']
        faculty = request.POST['faculty']
        department = request.POST['department']
        admission_number = request.POST['admission_number']
        room_number = request.POST['room_number']
        weight = request.POST['weight']
        height = request.POST['height']
        allergies = request.POST['allergies']
        medical_condition = request.POST['medical_condition']
        taking_medicationsyes = request.POST['taking_medicationsyes']
        taking_medicationsno = request.POST['taking_medicationsno']
        medications =  request.POST['medications']
        matric =  request.POST['matric']

        Patient = PatientRegistration()

        Patient.first_name = first_name
        Patient.save()
        Patient.last_name = last_name
        Patient.save()

        Patient.password = password
        Patient.save()


        Patient.comfirm_password = comfirm_password
        Patient.save()

        Patient.date_of_birth = date_of_birth
        Patient.save()

        Patient.email = email
        Patient.save()


        Patient.phone_number = phone_number
        Patient.save()

        Patient.gender = gender
        Patient.save()

        Patient.maritalstat = maritalstat
        Patient.save()

        Patient.faculty = faculty
        Patient.save()


        Patient.department = department
        Patient.save()


        Patient.admission_number = admission_number
        Patient.save()

        Patient.room_number = room_number
        Patient.save()

        Patient.weight = weight
        Patient.save()


        Patient.height = height
        Patient.save()

        Patient.allergies = allergies
        Patient.save()

        Patient.medical_condition = medical_condition
        Patient.save()

        Patient.taking_medicationsyes = medical_condition
        Patient.save()

        Patient.taking_medicationsno = taking_medicationsno
        Patient.save()

        Patient.medications = medications
        Patient.save()
        Patient.matric_num = matric
        Patient.save()

        messages.success(request, 'Successful Registration .')
        return HttpResponseRedirect(reverse('loginpage'))

    return render(request, 'patient_reg.html')

def patient_login_view(request):
    name = None
    redirect_to = request.POST.get('next', '')
    context_view = {}

    if request.method == 'POST':
        admission_number = request.POST['admission_number']
        password = request.POST['password']
        if not StaffRegistration.objects.filter(Id_number=admission_number):
            context_view["erro1"] = "Incorrect Email !"

        elif not StaffRegistration.objects.filter(Id_number=admission_number, password=password):
            context_view["erro1"] = "Incorrect Password!"
        else:
            userr = StaffRegistration.objects.get(Id_number=admission_number, password=password)
            hold = str(userr.id)
            request.session['name'] = hold
            if request.session.has_key('name') and redirect_to == '':
                #StaffRegistration.objects.filter(Id_number=admission_number, password=password)
                return HttpResponseRedirect(reverse('profile'))
            elif request.session.has_key('name') and redirect_to != '':
                #User_Model.objects.filter(email=e_mail, password=pass_w).update(login_times=now())
                return HttpResponseRedirect(redirect_to)

    return render(request, 'loginpage.html', context_view)





def p_login_view(request):
    namep = None
    redirect_to = request.POST.get('next', '')
    context_view = {}

    if request.method == 'POST':
        admission_number = request.POST['admission_number']
        password = request.POST['password']
        if not PatientRegistration.objects.filter(matric_num=admission_number):
            context_view["erro1"] = "Incorrect Email !"

        elif not PatientRegistration.objects.filter(matric_num=admission_number, password=password):
            context_view["erro1"] = "Incorrect Password!"
        else:
            userr = PatientRegistration.objects.get(matric_num=admission_number, password=password)
            hold = str(userr.id)
            request.session['namep'] = hold
            if request.session.has_key('namep') and redirect_to == '':
                #StaffRegistration.objects.filter(Id_number=admission_number, password=password)
                return HttpResponseRedirect(reverse('profilestudent'))
            elif request.session.has_key('namep') and redirect_to != '':
                #User_Model.objects.filter(email=e_mail, password=pass_w).update(login_times=now())
                return HttpResponseRedirect(redirect_to)

    return render(request, 'loginpage.html', context_view)


def bookapointment_view(request):
    time = request.session['namep']
    ussas = PatientRegistration.objects.get(id=time)
    # Assuming there's a one-to-one relationship between User and PatientRegistration
    st = StaffRegistration.objects.all()
    context = {'ussas': ussas,'st':st}
    return render(request,'bookApointment.html',context)  # Redirect to your login page URL


def apointmentDetails_view(request,id):
    time = request.session['namep']
    ussas = PatientRegistration.objects.get(id=time)
    # Assuming there's a one-to-one relationship between User and PatientRegistration
    sp = StaffRegistration.objects.get(id=id)
    context = {'ussas': ussas,'sp':sp}
    return render(request,'dr_setails.html',context)  # Redirect to your login page URL



def patient_logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('loginpage')  # Redirect to your login page URL

def staff_logout_view(request):
    del request.session['name']
    messages.info(request, "Logged Out!")
    return redirect('loginpage')  # Redirect to your login page URL




def staff_reg_view(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        comfirm_password = request.POST['comfirm_password']
        email = request.POST['email']
        admission_number = request.POST['admission_number']
        qualification = request.POST['qualification']

        admission_number = request.POST.get('admission_number', False)

        Staff = StaffRegistration()

        Staff.first_name = first_name
        Staff.save()
        Staff.last_name = last_name
        Staff.save()
        Staff.password = password
        Staff.save()

        Staff.email = email
        Staff.save()
        Staff.comfirm_password = comfirm_password
        Staff.save()
        Staff.qualification = qualification
        Staff.save()


        Staff.Id_number = admission_number
        Staff.save()


        messages.success(request, 'Successful Registration')
        return redirect('loginpage')  # Redirect to your login page URL

    return render(request, 'staff_reg.html')




    
def staff(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission_number, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')  # Redirect to your patient dashboard URL
            else:
                messages.error(request, 'Invalid admission number or password.')

    else:
        form = StaffLoginForm()

    # To display the current year
    current_year = datetime.datetime.now().year

    context = {
        'form': form,
        'current_year': current_year,
    }

    return render(request, 'staff.html', context)



# def subscribe(request):
#     if request.method == 'POST':
#         form = NewsletterForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             subscriber = form.save()

#             # Send welcome email
#             subject = 'Welcome to our Newsletter'
#             message = 'Thank you for subscribing to our newsletter!'
#             from_email = 'your_email@example.com'
#             to_email = [email]
#             send_mail(subject, message, from_email, to_email, fail_silently=False)

#             return redirect('index') 
#     else:
#         form = NewsletterForm()

#     return render(request, 'index.html', {'form': form})



@login_required  # Ensure the user is logged in
def profile(request):
    time = request.session['name']
    ussas = StaffRegistration.objects.get(id=time)
    # Assuming there's a one-to-one relationship between User and PatientRegistration

    context = {'ussas': ussas}
    return render(request, 'profile.html', context)




def profilestudent(request):
    time = request.session['namep']
    ussas = PatientRegistration.objects.get(id=time)
    # Assuming there's a one-to-one relationship between User and PatientRegistration

    context = {'ussas': ussas}
    return render(request, 'studentpro.html', context)






@login_required  # Ensure the user is logged in
def staff(request):
    # Assuming there's a one-to-one relationship between User and PatientRegistration
    try:
        staff_registrationt = StaffRegistration.objects.get(user=request.user)
    except StaffRegistration.DoesNotExist:
        # Handle the case where the patient registration doesn't exist
        staff_registrationt = None

    context = {'staffs': staff_registrationt}
    return render(request, 'staff.html', context)



def staff_login(request):
    if request.method == 'POST':
        form = StaffLoginForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            password = form.cleaned_data['password']
            user = authenticate(request, username=admission_number, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                return redirect('index')  # Redirect to your patient dashboard URL
            else:
                messages.error(request, 'Invalid admission number or password.')

    else:
        form = StaffLoginForm()

    # To display the current year
    current_year = datetime.datetime.now().year

    context = {
        'form': form,
        'current_year': current_year,
    }

    return render(request, 'staff_login.html', context)





def register(request):
    context = {}
    return render(request, 'register.html', context)


def login_page(request):
    context = {}
    return render(request, 'login_page.html', context)

def password_reset(request):
    context = {}
    return render(request, 'password_reset.html', context)


# @login_required
# def videocall(request):
#     return render(request, 'WEB_UIKITS.html', {"name" : request.user})

def videocall(request):
    user = request.user
    if user.is_authenticated:
        first_name = user.first_name
        last_name = user.last_name
        full_name = f"{first_name} {last_name}" if first_name and last_name else user.username
    else:
        full_name = "Guest"

    return render(request, 'WEB_UIKITS.html', {"name": full_name})

# views.py
# from django.shortcuts import render

# def join_video_call(request, room_id):
#     return render(request, 'join_video_call.html', {'room_id': room_id})

from django.shortcuts import render

def join_meeting(request):
    if request.method == 'POST':
        # Handle the form submission for joining a meeting
        room_id = request.POST.get('roomID')
        # Perform any necessary actions for joining a meeting

    return render(request, 'join_meeting.html')


