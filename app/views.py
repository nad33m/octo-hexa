"""
Definition of views.
"""
from datetime import datetime
from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from app.models import *
from app.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .tables import *
from rest_framework import viewsets
from .serializers import CsInfoSerializer
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    DeleteView
)
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )




def teacherlist(request):
    teachers = TeacherInfo.objects.select_related('scode').all()
    total_teachers = teachers.count()
    context = {
               'teachers': teachers,
               'total_teachers': total_teachers,
               
               } 
    return render(request, 'app/teachers.html', context)

class TeacherListView(ListView):
    model = TeacherInfo
    template_name = 'app/teachers.html'
    context_object_name = 'teachers'
    ordering = ['-created_at']

class TeacherDetailView(DetailView):
    model = TeacherInfo
    
class TeacherCreateView(CreateView):
    model = TeacherInfo
    fields = ['cnic', 'teacher_name', 'gender', 'father_name','qualification' ,'scode' ]
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TeacherDeleteView(DeleteView):
    model = TeacherInfo
    success_url = "/"


# class EmployeeCreateView(CreateView):
#     model = Employee
#     fields = ['first_name', 'last_name', 'mobile', 'email']

#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)

    # def form_valid(self, form):
    #     # You can print or log the cleaned data for debugging
    #     print("Form data is valid, saving the instance.")
    #     return super().form_valid(form)

    # def form_invalid(self, form):
    #     # If the form is invalid, you can debug by printing form errors
    #     print("Form is invalid.")
    #     print(form.errors)
    #     return super().form_invalid(form)


    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    

# def cscheck(request):
#     customer = customers.objects.all()
#     context = {
#                'title':'cs-details',
#                'customers' : customer,
#                'year':datetime.now().year,
#                'month': datetime.now().month
#             #    'form':form,   
#             #   'teachers': teachers,
#             #  'total_records' : total_records,
               
#                }
#     # return HttpRessponse('Hello world!')
#     return render(request, 'app/cscheck.html', context)

# def customerinfo(request):
#     customerForm = CustomersForm() 
#     context = {
#                'title':'cs-details',
#                'form': customerForm
               
#                } 
#     return render(request,"app/customer.html",context)  

# def customer_payments(request):
    # if request.method == 'POST':
    #     # The form is being submitted
    #     form = PaymentForm(request.POST)
    #     if form.is_valid():
    #         # If the form data is valid, save it to the database
    #         form.save()
    #         messages.success(request, 'Payment created successfully!')
    #         return redirect('add-payment-page')  # Replace with your desired redirect URL
    #     else:
    #         messages.warning(request, 'Customer with this check number already exists!')
    # else:
    #     # If the request is a GET request, display the blank form
    #     form = PaymentForm()

    # context = {
    #            'title':'',
    #            'form': form,
               
    #            } 
    # # Render the form template
    # return render(request, 'app/payments.html', context)
    # context = {
    #            'title':'cs-details',
    #            'form': Payment_Form,
               
    #            } 
    # return render(request,"app/payments.html",context)  

# def testing_db(request):
#     # schools = csinfo.objects.all().order_by('scode')
#     q = request.GET.get('q')
#      # get the scode from the input box
#     if q:
#         q = q[:100]
#         q = escape(q)
#     else:
#         q=' '
    
#     if q:
#         # artists = Artist.objects.filter(name__icontains=url_parameter)
#         # schools = csinfo.objects.filter(Q(scode__icontains=q) | Q(sname__icontains=q))
#         schools = csinfo.objects.filter(Q(scode__icontains=q) | Q(sname__icontains=q))
#         total_records = schools.count
#         teachers = cst042024.objects.filter(scode__in=schools.values_list('scode', flat=True))
#         # teachers = cst042024.objects.filter(scode=q)
#         # teachers = cst042024.objects.all()
#         # dataentry = dataentry.filter(Q(bemiscode__icontains=q) | Q(schoolname__icontains=q))
#     # form = csinfoForm()
    
#     # if request.method == 'POST':
#     #     form = csinfoForm(request.POST)
#     #     if form.is_valid():
#     #         form.save()
#     #     return redirect ('/')

#     context = {'schools': schools,
#             #    'form':form,   
#                'teachers': teachers,
#                'total_records' : total_records,
               
#                }
#     # return HttpRessponse('Hello world!')
#     return render(request, 'cssearch/testing.html', context)


# def teacher_show(request, pk):
#     teachers = cst042024.objects.filter(scode=pk)
#     context = {
#                # 'form':form,   
#                'teachers': teachers,
#                }
    
#     return render(request, 'cssearch/teachers.html', context)


def add_teachers(request):
    if request.method == 'POST':
        # The form is being submitted
        form = TeacherForm(request.POST)
        if form.is_valid():
            # If the form data is valid, save it to the database
            form.save()
            messages.success(request, 'New teacher added successfully!')
            return redirect('add-teachers-page')  # Replace with your desired redirect URL
        else:
            messages.warning(request, 'Customer with this check number already exists!')
    else:
        # If the request is a GET request, display the blank form
        form = TeacherForm()

    context = {
               'title':'',
               'form': form,
               
               } 
    # Render the form template
    return render(request, 'app/add_teachers.html', context)

# def list(request):
# 	model = TeacherInfo.objects.select_related('school_code_id').all
# 	table = MyTable(model)
# 	return render(request=request, template_name="app/table.html", context={"model":model, "table":table})

def teacherlist(request):
    # teachers = TeacherInfo.objects.select_related('school_code').all()  # Add parentheses to call the all() method
    # teachers = TeacherInfo.objects.prefetch_related('school_code').all()
    teachers = TeacherInfo.objects.select_related('scode').all()
    # for teacher in teachers:
    #     print(teacher.teacher_name, teacher.school_code)
    
    total_teachers = teachers.count()
    
    print("Total teachers: ", total_teachers)  
    context = {
               'teachers': teachers,
               'total_teachers': total_teachers,
               
               } 

    return render(request, 'app/teachers.html', context)

def deleteteacher(request, cnic):
  teacher = TeacherInfo.objects.get(cnic=cnic)
  teacher.delete()
  return HttpResponseRedirect(reverse('show-teachers-page'))


class BlogPostViewSet(viewsets.ModelViewSet):
	queryset = CsInfo.objects.all()
	serializer_class = CsInfoSerializer
     
