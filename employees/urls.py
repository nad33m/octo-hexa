from django.urls import path
from employees import views 
from employees.views import (
    EmpbasicinfoCreateView,
   
)



urlpatterns = [
    # path("", views.homepage , name="emp-home"),
    path('', EmpbasicinfoCreateView.as_view() , name='create-employee'),

]