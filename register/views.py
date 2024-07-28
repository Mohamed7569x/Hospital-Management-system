from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Patient
from .forms import PatientForm, VerifyForm

def register(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
             try:
                data_ = Patient(firstname=form.cleaned_data['first_name'],
                    lastname=form.cleaned_data['last_name'],
                    dob=form.cleaned_data['dob'],
                    Gender=form.cleaned_data['gender'],
                    Phone=form.cleaned_data['phone'],
                    Email=form.cleaned_data['email'],
                    Address=form.cleaned_data['address'],
                    Emergency_Contact=form.cleaned_data['emergency_contact'],
                    Medical_History=form.cleaned_data['medical_history']
                    )
                
                data_.save()
                return redirect('register')
             except:
                form.add_error(None, "Email or phone number already in use.")
        else:
            if not form.errors:
                form.add_error(None, "Email or phone number already in use.")
        return render(request, 'register.html', {'form': form})
    else:
        form = PatientForm()
             
    return render(request, 'register.html', {'form': form})

def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def verify(request):
    search_performed = False
    if request.method == 'POST':
        
        form = VerifyForm(request.POST)
        if form.is_valid():
            search_performed = True
            search_box = form.cleaned_data['search_box']
            try:
                x = Patient.objects.get(id=search_box)
            except:
                x = None
            try:
                y = Patient.objects.get(firstname=search_box)
            except:
                y = None
            try:
                z = Patient.objects.get(Email=search_box)
            except:
                z = None
            try:   
                j = Patient.objects.get(Phone=search_box)
                
            except:
                j = None
            if x or y or z or j:
                if x:
                    form_ = x
                if y:
                    form_ = y
                if z:
                    form_ = z
                if j:
                    form_ = j
                context = {
        'form': form,
        'patient': form_,
        'search_performed': search_performed
    }
                return render(request, 'verify.html', context)
        else:
            print(form.errors)
    else:
        form = VerifyForm()
        
    context = {
        'form': form,
        'search_performed': search_performed
    }    
    return render(request, 'verify.html', context)



def dashboard(request):
    
    patients = Patient.objects.all()
    if request.method == 'POST':
        if 'delete' in request.POST: 
            id_ = request.POST.get("delete")
            delete_object = Patient.objects.get(id=id_)
            delete_object.delete()
    return render(request, 'dashboard.html', {'patients': patients})

