from django.shortcuts import render,redirect
from .forms import ContactForm

# Create your views here.
def index(request):
    form=ContactForm()
    if request.method == "POST":
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('model')
    return render(request,'index.html',{'form':form})