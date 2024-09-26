"""
Definition of forms.
"""
from app.models import *
from django.utils.translation import gettext_lazy as _
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from app.models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Row, Column, Button
from django_select2.forms import ModelSelect2Widget
class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class TeacherForm(forms.ModelForm):
    # school_code = forms.ModelChoiceField(
    #     queryset=CsInfo.objects.all(),
    #     label="School Name",
    #     widget=ModelSelect2Widget(
    #         model=CsInfo,
    #         search_fields=['sname__icontains'],  # Search by school name
    #         attrs={'data-placeholder': 'Search for a school...'}
    #     )
    # )

    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))

    class Meta:
        model = TeacherInfo
        fields = "__all__"

    
    
class EmployeeForm(forms.ModelForm):  
  
    class Meta:  
        # To specify the model to be used to create form  
        model = Employee  
        # It includes all the fields of model  
        fields = '__all__'  

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # Initialize FormHelper
    #     self.helper = FormHelper()

    #     # Define the layout
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('customernumber', css_class='col-md-4'),
    #             Column('customername', css_class='col-md-4'),
    #             Column('contactlastname', css_class='col-md-4'),
                
    #         ),
    #         Row(
    #         Column('addressline1',css_class='col-md-6'),
    #         Column('addressline2',css_class='col-md-6'),
    #         ),
    #         Row(
    #             Column('state', css_class='col-md-4'),
    #             Column('postalcode', css_class='col-md-4'),
    #             Column('country', css_class='col-md-4'),
    #         ),
    #         Row(
    #             Column('salesrepemployeenumber', css_class='col-md-6'),
    #             Column('creditlimit', css_class='col-md-6'),
    #         ),
    #         Div(
    #             Field('asfdsaf', css_class="bg-danger border-2 border-top border-danger")
    #         ),
    #         Div(
    #             Submit('submit', 'Submit', css_class='btn-primary'),
    #             Button('cancel', 'Cancel', css_class='btn-danger'),
    #             css_class='form-group'
    #         ),
    #     )

# class csinfoForm(forms.ModelForm):
    
    # customernumber = forms.ModelChoiceField(
    #     queryset=customers.objects.all(),
    #     label="Customer",
    #     to_field_name="customernumber",
    #     widget=forms.Select
    # )

    # paymentdate = forms.DateField(
    #     widget=forms.DateInput(attrs={'type': 'date'}),
    #     label="Payment Date"
    # )

    # class Meta:
    #     model = TeacherInfo
    #     fields = "__all__"

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     # Customize the label to show customer name and number
    #     self.fields['customernumber'].label_from_instance = lambda obj: f"{obj.customername} ({obj.customernumber})"

    #     # Initialize FormHelper
    #     self.helper = FormHelper()

    #     # Define the layout
    #     self.helper.layout = Layout( 
    #         Row(
    #             Column('customernumber',css_class='col-md-12'),
    #         ),
    #         Row(
    #             Column('checknumber',css_class='col-md-12'),
    #         ),
    #         Row(
    #             Column('paymentdate',css_class='col-md-6'),
    #             Column('amount',css_class='col-md-6'),
    #         ),
    #          Div(
    #             Submit('submit', 'Save', css_class='btn-primary'),
    #             Button('cancel', 'Cancel', css_class='btn-danger'),
    #             css_class='form-group'
    #         ),
    #     )


