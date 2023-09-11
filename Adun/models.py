from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel/%y/%m/%d/')
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=200)
    
    def __str__(self):
        return self.title
    

class OpeningHours(models.Model):
    day1 = models.CharField(max_length=20, default='Mon - Fri')
    hours1 = models.CharField(max_length=50)
    day2 = models.CharField(max_length=20)
    hours2 = models.CharField(max_length=50)
    day3 = models.CharField(max_length=20)
    hours3 = models.CharField(max_length=50)

    def __str__(self):
        return self.day1
    
class Appoint_contact(models.Model):
    description = models.TextField(max_length="150")
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return "Appoint_contact"

class AboutContent(models.Model):
    title = models.CharField(max_length=200,  default='Say Something nice')
    subtitle = models.CharField(max_length=200)
    intro_text = models.TextField()
    image_url = models.ImageField(upload_to='AboutUs/%y/%m/%d/')

    def __str__(self):
        return "About Us"

class ApointmentContent(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return "Apointment_Text"
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.ImageField(upload_to='Service/%y/%m/%d/')

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    testimonial_text = models.TextField()
    image_url = models.ImageField(upload_to='Testimonial/%y/%m/%d/')

    def __str__(self):
        return self.client_name
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Team/%y/%m/%d/')
    
    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
    
  


class PatientRegistration(models.Model):
    matric_num = models.CharField(max_length=50, null=True,blank=True)
    user = models.CharField(max_length=50, null=True,blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=30, unique=True, null=True)
    comfirm_password = models.CharField(max_length=30, unique=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True, blank=True)
    GENDER_CHOICES = [
        ('Gender', 'Gender'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    gender = models.CharField(max_length=90, choices=GENDER_CHOICES,null=True)
    
    
    
    MARITAL_STATUS_CHOICES = [
        ('Select', 'Select'),
        ('Gender', 'Gender'),
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorced', 'Divorced'),
    ]
    maritalstat = models.CharField(max_length=100, choices=MARITAL_STATUS_CHOICES,  null=True)

    FACULTY_CHOICES = [
        ( 'Faculty','Faculty'),
        ( 'Faculty of Science','Faculty of Science'),
        ( 'Faculty of Arts and Management Science','Faculty of Arts and Management Science'),
        ( 'Faculty of Law','Faculty of Law'),
    ]
    faculty = models.CharField(max_length=200, choices=FACULTY_CHOICES,null=True)
    
    DEPARTMENT_CHOICES = [
        ( 'Select','Select'),
        ( 'Department of Biology and Forensic Science','Department of Biology and Forensic Science'),
        ( 'Department of Computing Science','Department of Computing Science'),
        ( 'Department of Public Law and Private Law','Department of Public Law and Private Law'),
        ( 'Department of Accounting/Business Administration/Economics','Department of Accounting/Business Administration/Economics'),
        ( 'Department of English & Literary Studies/History & International Studies','Department of English & Literary Studies/History & International Studies'),
        ( 'Department of International Relations/Hospitality & Tourism Studies','Department of International Relations/Hospitality & Tourism Studies'),
    ]
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES,null=True)
    
    admission_number = models.CharField(max_length=20,null=True)
    room_number = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100000)],null=True)

    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    allergies = models.TextField(null=True)
    medical_condition = models.TextField(null=True)
    taking_medications = models.BooleanField( null=True)
    medications = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    def __str__(self):
        return self.user.username



level_type = (
    ('Select', 'Select'),
    ('Doctor', 'Doctor'),
    ('Nurse', 'Nurse'),
    ('Pharmacist', 'Pharmacist'),
    ('Consultant', 'Consultant'),
    ('Laboratory', 'Laboratory'),

)
class StaffRegistration(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff', null=True)

    Id_number = models.CharField(max_length=50, null=True,blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=900, null=True)
    comfirm_password = models.CharField(max_length=900, null=True)
    #date_of_birth = models.DateField()
    email = models.EmailField()

    qualification = models.CharField(choices=level_type, max_length=100, default="Select")
    
    #Services_Rendered = models.TextField(max_length=250,null=True)
    #weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    #height = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    #allergies = models.TextField(null=True)
    #medical_condition = models.TextField(null=True)
    #taking_medications = models.BooleanField( null=True)
    #medications = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}"



class AppointmentModel(models.Model):
    booked = models.BooleanField(default=False)

    patient = models.ForeignKey(PatientRegistration, null=True, blank=True, on_delete=models.SET_NULL, related_name='patient')
    staff= models.ForeignKey(StaffRegistration, null=True, blank=True, on_delete=models.SET_NULL, related_name='staff')


    def __str__(self):
        return f"{self.patient}"


