from django.shortcuts import render
from .models import *
# Create your views here.
#function for getting all about info
def index(request):
    all_info = Info.objects.all()
    all_skills = Skills.objects.all()
    all_projects = Project.objects.all()
    return render(request,"layout.html",{
        "all_info":all_info,
        "all_skills":all_skills,
        "all_projects":all_projects,
    })