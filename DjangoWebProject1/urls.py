"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from app.views import (
    # EmployeeCreateView,
    TeacherListView, 
    TeacherDetailView, 
    TeacherCreateView,
    TeacherDeleteView
)

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('emp/', include("employees.urls")), 
    # path('customerinfo/', views.customerinfo, name='c-info'),
    # path('payment/', views.customer_payments, name='add-payment-page'),
    path('addteachers/', views.add_teachers, name='add-teachers-page'),
    # path('teacherlisting/', views.teacherlist, name='show-teachers-page'),

    path('teacherlisting/', TeacherListView.as_view(), name='show-teachers-page'),
    path('teacher/<str:pk>', TeacherDetailView.as_view(), name='teacher-detail-page'),
    path('createteacher/', TeacherCreateView.as_view() , name='create-teacher'),
    path('delteacher/<str:pk>', TeacherDeleteView.as_view(), name='delete-teacher'),
    

    # path('createemp/', EmployeeCreateView.as_view() , name='create-employee'),



    # path('delete-teacher/<str:cnic>', views.deleteteacher, name='delete-teacher'),
    # path("table", views.list, name="list"),
    # path("select2/", include("django_select2.urls")),
    # path('cscheck/', views.cscheck, name='cs-details'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
