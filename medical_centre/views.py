from django.shortcuts import render

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

        about = request.POST.get('about')

        print(first_name,last_name,age,sex,phone,email,addiction_period,addicted_drugs,type_of_addiction,medications_taken_prior,about)

    return render(request, 'medical/create_patient.html')