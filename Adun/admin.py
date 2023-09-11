from django.contrib import admin

from .models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Import UserAdmin if your model inherits from AbstractUser
from .models import PatientRegistration

# class CustomUserAdmin(UserAdmin):
#     list_display = ('email', 'first_name', 'last_name', 'date_of_birth', 'phone_number')  # Customize the fields you want to display in the admin list view

# # Register the PatientRegistration model with the CustomUserAdmin class
# admin.site.register(PatientRegistration, CustomUserAdmin)


admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(CarouselItem)
admin.site.register(AboutContent)
admin.site.register(OpeningHours)
admin.site.register(Appoint_contact)
admin.site.register(ApointmentContent)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(TeamMember)
admin.site.register(PatientRegistration)
admin.site.register(StaffRegistration)
# admin.site.register(PatientRegistration)


