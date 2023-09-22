from django.shortcuts import render,redirect
from database.models import patient_info
from django.contrib import messages
import csv,io

# Create your views here.
def hosp_dash(request):
    return render(request, 'medical/dash.html')

def patient_add(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        phone = request.POST.get('phone_number')
        email = request.POST.get('email')
        addiction_period = request.POST.get('addiction_period')
        addicted_drugs = request.POST.get('addicted_drugs')
        type_of_addiction = request.POST.get('type_of_addiction')
        medications_taken_prior = request.POST.get('medications_taken_prior')

        medical_history = {"addiction_period":addiction_period, "addicted_drugs":addicted_drugs, "type_of_addiction":type_of_addiction, "medications_taken_prior":medications_taken_prior}


        about = request.POST.get('about')

        patient_info_add = patient_info(
            f_name = first_name,
            l_name = last_name,
            age = age,
            sex = sex,
            phone = phone,
            email = email,
            medical_history = str(medical_history),
            about = about
        )
        patient_info_add.save()
        messages.success(request, 'Patient added successfully')
        return redirect('hospital_dashboard')

    return render(request, 'medical/create_patient.html')

def view_patient(request):
    patient_info_obj = patient_info.objects.all()
    context = {
        "patient_info_obj":patient_info_obj
    }
    return render(request, 'medical/view_patient.html', context)

def bulk_add(request):
    if request.method == "POST":
        file = request.FILES['data']
        if not file.name.endswith(".csv"):
            messages.error(request, 'Please upload a csv file')
            return redirect('bulk_add')
        
        data = file.read().decode("utf-8")
        io_string = io.StringIO(data)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            medical_history = {"addiction_period":column[6], "addicted_drugs":column[7], "type_of_addiction":column[8], "medications_taken_prior":column[9]}
            
            created = patient_info.objects.create(
                f_name = column[0],
                l_name = column[1],
                age = column[2],
                sex = column[3],
                phone = column[4],
                email = column[5],
                medical_history = str(medical_history),
                about = column[10]
            )
            created.save()
        messages.success(request, 'Patients added successfully')
        return redirect('hospital_dashboard')
    return render(request, 'medical/import_data.html')