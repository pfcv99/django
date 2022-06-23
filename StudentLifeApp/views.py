from django.shortcuts import render
from django.shortcuts import redirect  # new
from .forms import studentsForm  # new
from .models import students  # new
from django.contrib import messages  # new

# Create your views here.
def addstudents(request):
    if request.method == "POST":
        fm = studentsForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Student Added Successfully')

    fm = studentsForm()
    studata = students.objects.all()
    return render(request, 'index.html', context={'fm': fm, 'studata': studata})

def deletestudents(request, id):
    students.objects.get(pk=id).delete()
    messages.success(request, 'Student Record Deleted')
    return redirect('/')

def edit(request, id):
    instance = students.objects.get(pk=id)
    if request.method == "POST":
        fm = studentsForm(request.POST, instance=instance)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Student Record Updated')
            return redirect('/')
            
    fm = studentsForm(instance=instance)
    return render(request, 'edit.html', context={'fm': fm})
