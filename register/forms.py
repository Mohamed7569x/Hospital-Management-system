# forms.py
from django import forms

class PatientForm(forms.Form):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(label='Date of Birth', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(label='Gender', choices=[('Male', 'Male'), ('Female', 'Female')], widget=forms.Select(attrs={'class': 'form-control'}))
    phone = forms.CharField(label='Phone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=False, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_contact = forms.CharField(label='Emergency Contact', widget=forms.TextInput(attrs={'class': 'form-control'}))
    medical_history = forms.CharField(label='Medical History', widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    
class VerifyForm(forms.Form):
    search_box = forms.CharField(label='search_box', widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    

