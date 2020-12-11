from django.shortcuts import render
from .models import Project

# Create your views here.
def home(request):

    # get all the models from database of this class
    projects = Project.objects.all()

    return render(request, 'portfolio/home.html', {'projects':projects})
