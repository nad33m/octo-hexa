
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class customers(models.Model):
    customernumber = models.IntegerField(db_column='customerNumber', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='customerName', max_length=50)  # Field name made lowercase.
    contactlastname = models.CharField(db_column='contactLastName', max_length=50)  # Field name made lowercase.
    contactfirstname = models.CharField(db_column='contactFirstName', max_length=50)  # Field name made lowercase.
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True)  # Field name made lowercase. 
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, blank=True, null=True)
    postalcode = models.CharField(db_column='postalCode', max_length=15, blank=True, null=True)  # Field name made lowercase.     
    country = models.CharField(max_length=50)
    salesrepemployeenumber = models.IntegerField(db_column='salesRepEmployeeNumber', blank=True, null=True)  # Field name made lowercase.
    creditlimit = models.DecimalField(db_column='creditLimit', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'
    
    def __str__(self):
        return f"{self.customername}, {self.city}"

class offices(models.Model):
    officecode = models.CharField(db_column='officeCode', primary_key=True, max_length=10)  # Field name made lowercase.
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    addressline1 = models.CharField(db_column='addressLine1', max_length=50)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='addressLine2', max_length=50, blank=True, null=True)  # Field name made lowercase. 
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50)
    postalcode = models.CharField(db_column='postalCode', max_length=15)  # Field name made lowercase.
    territory = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'offices'
    
    
    
class employees(models.Model):
    employeenumber = models.IntegerField(db_column='employeeNumber', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=50)  # Field name made lowercase.
    extension = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    # officecode = models.CharField(db_column='officeCode', max_length=10)  # Field name made lowercase.
    officecode = models.ForeignKey(offices, on_delete=models.CASCADE, db_column='officeCode') 
    reportsto = models.IntegerField(db_column='reportsTo', blank=True, null=True)  # Field name made lowercase.
    jobtitle = models.CharField(db_column='jobTitle', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'
    
    def __str__(self):
        return f"{self.firstname}, {self.lastname}"

class orderdetails(models.Model):
    ordernumber = models.IntegerField(db_column='orderNumber', primary_key=True)  # Field name made lowercase. The composite primary key (orderNumber, productCode) found, that is not supported. The first column is selected.
    productcode = models.CharField(db_column='productCode', max_length=15)  # Field name made lowercase.
    quantityordered = models.IntegerField(db_column='quantityOrdered')  # Field name made lowercase.
    priceeach = models.DecimalField(db_column='priceEach', max_digits=10, decimal_places=2)  # Field name made lowercase.
    orderlinenumber = models.SmallIntegerField(db_column='orderLineNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetails'
        unique_together = (('ordernumber', 'productcode'),)


class orders(models.Model):
    ordernumber = models.IntegerField(db_column='orderNumber', primary_key=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate')  # Field name made lowercase.
    requireddate = models.DateField(db_column='requiredDate')  # Field name made lowercase.
    shippeddate = models.DateField(db_column='shippedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=15)
    comments = models.TextField(blank=True, null=True)
    # customernumber = models.IntegerField(db_column='customerNumber')  # Field name made lowercase.
    customernumber = models.ForeignKey(customers, on_delete=models.CASCADE, db_column='customerNumber') 
    
    class Meta:
        managed = False
        db_table = 'orders'

class payments(models.Model):
    customernumber = models.ForeignKey(customers, on_delete=models.CASCADE, db_column='customerNumber')  
    # customernumber = models.IntegerField(db_column='customerNumber', primary_key=True)  # Field name made lowercase. The composite primary key (customerNumber, checkNumber) found, that is not supported. The first column is selected.
    checknumber = models.CharField(db_column='checkNumber', max_length=50)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='paymentDate')  # Field name made lowercase.
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'payments'
        unique_together = (('customernumber', 'checknumber'),)

    def __str__(self):
        return f"{customers.customername}, {self.checknumber}"

class productlines(models.Model):
    productline = models.CharField(db_column='productLine', primary_key=True, max_length=50)  # Field name made lowercase.        
    textdescription = models.CharField(db_column='textDescription', max_length=4000, blank=True, null=True)  # Field name made lowercase.
    htmldescription = models.TextField(db_column='htmlDescription', blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # managed = False 
        db_table = 'productlines'

class products(models.Model):
    productcode = models.CharField(db_column='productCode', primary_key=True, max_length=15)  # Field name made lowercase.        
    productname = models.CharField(db_column='productName', max_length=70)  # Field name made lowercase.
    productline = models.CharField(db_column='productLine', max_length=50)  # Field name made lowercase.
    productscale = models.CharField(db_column='productScale', max_length=10)  # Field name made lowercase.
    productvendor = models.CharField(db_column='productVendor', max_length=50)  # Field name made lowercase.
    productdescription = models.TextField(db_column='productDescription')  # Field name made lowercase.
    quantityinstock = models.SmallIntegerField(db_column='quantityInStock')  # Field name made lowercase.
    buyprice = models.DecimalField(db_column='buyPrice', max_digits=10, decimal_places=2)  # Field name made lowercase.
    msrp = models.DecimalField(db_column='MSRP', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'