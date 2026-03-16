from django.shortcuts import render
from django.views.generic import TemplateView,ListView,UpdateView,CreateView,DeleteView
from .models import Details
from .forms import DetailView

# Create your views here.

class IndexView(ListView):
    template_name='generic/index.html'
    model=Details
    context_object_name='data'
    
class CreateDataView(CreateView):
    template_name='generic/forms.html'
    model=Details
    form_class=DetailView
    success_url='/generic'
    
class UpdateDataView(UpdateView):
    template_name='generic/forms.html'
    model=Details
    form_class=DetailView
    success_url='/generic'
    
class DeleteDataView(DeleteView):
    model=Details
    success_url='/generic'
