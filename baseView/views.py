from django.shortcuts import render,redirect
from django.views import View
from .models import contact1

class indexView(View):
    def get(self, request):
        data=contact1.objects.all()
        return render (request,'baseViews/index.html',{'data':data})
    
    def post(self,request):
        name=request.POST.get('name')
        age=request.POST.get('age')
        contact1.objects.create(name=name,age=age)
        return redirect('indexview')


