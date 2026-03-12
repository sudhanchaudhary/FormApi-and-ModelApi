from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def home(request):
    form=StudentForm()
    if request.method == "POST":
        form=StudentForm(data=request.POST)
        if form.is_valid():
            name=form.cleaned_data.get('name')
            age=form.cleaned_data.get('age')
            password=form.cleaned_data.get('password')
            gender=form.cleaned_data.get('gender')
            subject=form.cleaned_data.get('subject')
            Student.objects.create(name=name,age=age,password=password,gender=gender,subject=subject)
            return redirect('home')
    return render(request,'home.html',{'form':form})