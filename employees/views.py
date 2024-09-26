from django.shortcuts import render
from datetime import datetime
from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from datetime import datetime
from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.urls import reverse
from employees.models import *
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    DeleteView
)

# Create your views here.
def homepage(request):
    
    teachers = "my name is nadeem"
    total_teachers = 132422

    context = {
                'teachers': teachers,
                'total_teachers': total_teachers,
               } 
    return render(request, 'employees/home.html', context)

class EmpbasicinfoCreateView(CreateView):
    model = empbasicinfo
    fields = ['emp_name','father_name','gender','cnic','designation','bps','date_of_birth','date_of_joining']
    
    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})
        form.fields['date_of_joining'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)