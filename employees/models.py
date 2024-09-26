from django.db import models
from datetime import datetime, timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class empbasicinfo(models.Model):

    class gender(models.TextChoices):
        MALE = 'Male', ('Male')
        FEMALE = 'Female', ('Female')
    
    emp_name = models.CharField(max_length=255, blank=False, null=False)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=6, blank=True, null=True, choices=gender.choices)
    cnic =  models.CharField(max_length=16, unique=True, primary_key=True)
    designation = models.CharField(max_length=255, blank=False, null=False)
    bps = models.CharField(max_length=2, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete = models.CASCADE )
   
    class Meta:
        db_table = 'empbasicinfo'

    def __str__(self):
        return f"{self.emp_name}, {self.cnic}"
    
class empsalary(models.Model):

    # class months(models.TextChoices):
    #     MALE = 'Male', ('Male')
    #     FEMALE = 'Female', ('Female')
    
    sal_month = models.CharField(max_length=25, blank=False, null=False)
    sal_year = models.CharField(max_length=4, blank=False, null=False)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    ntn = models.CharField(max_length=50, blank=True, null=True)
    account_no = models.CharField(max_length=125, blank=True, null=True)
    basic_sal = models.IntegerField(blank=False, null=False) 
    med_allowance = models.IntegerField(blank=True, null=True)
    convence_allowance = models.IntegerField(blank=True, null=True)
    house_rent = models.IntegerField(blank=True, null=True)
    dra_2015 = models.IntegerField(blank=True, null=True)
    ara_2022 = models.IntegerField(blank=True, null=True)
    ara_2023 = models.IntegerField(blank=True, null=True)
    ara_2014 = models.IntegerField(blank=True, null=True)
    special_allowance = models.IntegerField(blank=True, null=True)
    utility_allowance = models.IntegerField(blank=True, null=True)
    totall = models.IntegerField(blank=True, null=True)
    provident_fund_emp = models.IntegerField(blank=True, null=True)
    provident_fund_bef = models.IntegerField(blank=True, null=True)
    provident_fund_balance = models.IntegerField(blank=True, null=True)
    pfcm = models.IntegerField(blank=True, null=True)
    cpfb = models.IntegerField(blank=True, null=True)
    wdpf = models.IntegerField(blank=True, null=True)
    profit = models.IntegerField(blank=True, null=True)
    apfb = models.IntegerField(blank=True, null=True)
    eobi_emp = models.IntegerField(blank=True, null=True)
    eobi_bef =models.IntegerField(blank=True, null=True)
    atp =models.IntegerField(blank=True, null=True)
    income_tax =models.IntegerField(blank=True, null=True)
    total_deduction =models.IntegerField(blank=True, null=True)
    net_salary = models.IntegerField(blank=True, null=True)
    adhoc_allowance = models.IntegerField(blank=True, null=True)
    group_insurance = models.IntegerField(blank=True, null=True)
    cnic= models.ForeignKey(empbasicinfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete = models.CASCADE )
    
    class Meta:
        db_table = 'empsalary'

    def __str__(self):
        return f"{self.cnic}, {self.totall}"






