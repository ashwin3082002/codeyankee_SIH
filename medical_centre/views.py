from django.shortcuts import render
from database.models import patient_info

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

        return render(request, 'medical/dash.html')

    return render(request, 'medical/create_patient.html')