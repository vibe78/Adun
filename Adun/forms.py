
from django import forms
from .models import *
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']



from django import forms
from django.contrib.auth.models import User
from .models import PatientRegistration

class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = PatientRegistration
        exclude = ['user']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")

        # Add any other password complexity validation here

        return cleaned_data

class PatientLoginForm(forms.Form):
    admission_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)



    
    
# class StaffRegistrationForm(forms.ModelForm):
#     class Meta:
#         model = StaffRegistration
#         fields = '__all__'

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         comfirm_password = cleaned_data.get("comfirm_password")

#         if password != comfirm_password:
#             raise ValidationError("Passwords do not match.")

#         # Add any other password complexity validation here

#         return cleaned_data




class StaffRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = StaffRegistration
        fields ='__all__'




class StaffLoginForm(forms.Form):
    admission_number = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)