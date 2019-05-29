from django.shortcuts import render
from django.http import HttpResponse
from site_app.models import Student
from site_app.models import Intereste

def contact(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Reason = request.POST.get('reason')
        Message = request.POST.get('message')


        s = Student(Name=Name,Email=Email,Reason=Reason,Message=Message)
        s.save()
    return render(request, 'site_app/contact.html')


def index(request):
    return render(request, 'site_app/index.html')

def profile(request):
    skillset = Intereste.objects.all()
    skill_dict = {'acc_records':skillset}
    return render(request, 'site_app/profile.html', context=skill_dict)

# Create your views here.
