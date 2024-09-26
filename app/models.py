# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from datetime import datetime, timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class CsInfo(models.Model):

    class Category(models.TextChoices):
        SUMMER = 'Summer', ('Summer')
        WINTER = 'Winter', ('Winter')
    
    class Regions(models.TextChoices):
        CENTRAL_A = 'Central-A', ('Central-A')
        CENTRAL_B = 'Central-B', ('Central-B')
        SOUTHWEST_A = 'South West-A', ('South West-A')
        SOUTHWEST_B = 'South West-B', ('South West-B')
        SOUTHEAST_A = 'South East-A', ('South East-A')
        SOUTHEAST_B = 'South East-B', ('South East-B')
        NORTH_A = 'North-A', ('North-A')
        NORTH_B = 'North-B', ('North-B')
        
    scode = models.CharField(max_length=255, unique=True, primary_key=True)  # Field name made lowercase.
    cat = models.CharField(db_column='Cat', max_length=255, blank=True, null=True, choices=Category.choices)  # Field name made lowercase.
    did = models.CharField(db_column='DID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tid = models.CharField(db_column='TID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ucid = models.CharField(db_column='UCID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    vid = models.CharField(db_column='VID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase = models.CharField(db_column='Phase', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sname = models.CharField(db_column='Sname', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True, choices=Regions.choices)
    schoolstatus = models.CharField(db_column='SchoolStatus', max_length=16, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'cs_info'

    def __str__(self):
        return f"{self.sname}, {self.scode}"


class TeacherInfo(models.Model):

    class AcademicQualification(models.TextChoices):
        MATRIC = 'Matric', ('Matric')
        INTER = 'Inter', ('Intermediate')
        GRADUATE = 'Graduate', ('Graduate')
        MASTERS = 'Masters', ('Mssters')
    
    # school_code = models.FloatField(blank=True, null=True)
    cnic = models.CharField(max_length=255,unique=True,primary_key=True)
    expiry_date = models.CharField(max_length=255, blank=True, null=True)
    teacher_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    account_no = models.CharField(max_length=255, blank=True, null=True)
    bank_code = models.FloatField(blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    branch_code = models.CharField(max_length=255, blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    contact_no = models.CharField(max_length=255, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    qualification = models.CharField(max_length=255, blank=True, null=True, choices= AcademicQualification)
    profq = models.CharField(max_length=255, blank=True, null=True)
    appointment_date = models.DateTimeField(blank=True, null=True)
    birth_date = models.CharField(max_length=255, blank=True, null=True)
    scode= models.ForeignKey(CsInfo, on_delete=models.CASCADE,db_column='scode')
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # date = models.DateTimeField(auto_now_add=True, blank=True)
    # date = models.DateTimeField(default=datetime.now, blank=True)
  
    
    class Meta:
        db_table = 'teacher_info'

    def __str__(self):
        return f"{self.scode}, {self.cnic}, {self.teacher_name}"

    def get_absolute_url(self):
        return reverse('show-teachers-page')
    
class Constructedschools(models.Model):
    bemis_code = models.ForeignKey(CsInfo, on_delete=models.CASCADE, db_column='scode')
    # bemis_code = models.CharField(db_column='BEMIS Code', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cat = models.CharField(db_column='Cat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tehsil = models.CharField(db_column='Tehsil', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uc = models.CharField(db_column='UC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    village = models.CharField(db_column='Village', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phase = models.CharField(db_column='PHASE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    school_name = models.CharField(db_column='School Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    constructed = models.CharField(db_column='Constructed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coordinates_n = models.CharField(db_column='Coordinates n', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    coordinates_e = models.CharField(db_column='Coordinates E', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'constructedschools'

    def __str__(self):
        return f"{self.bemis_code}, {self.school_name}"


class CsEnrollment(models.Model):
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tehsil = models.CharField(db_column='Tehsil', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uc = models.CharField(db_column='UC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    # bemis_code = models.CharField(db_column='BEMIS_Code', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bemis_code = models.ForeignKey(CsInfo, on_delete=models.CASCADE, db_column='scode')
    school_name = models.CharField(db_column='School_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    girls_kachi = models.FloatField(db_column='Girls_Kachi', blank=True, null=True)  # Field name made lowercase.
    girls_one = models.FloatField(db_column='Girls_One', blank=True, null=True)  # Field name made lowercase.
    girls_two = models.FloatField(db_column='Girls_Two', blank=True, null=True)  # Field name made lowercase.
    girls_three = models.FloatField(db_column='Girls_Three', blank=True, null=True)  # Field name made lowercase.
    girls_four = models.FloatField(db_column='Girls_four', blank=True, null=True)  # Field name made lowercase.
    girls_five = models.FloatField(db_column='Girls_five', blank=True, null=True)  # Field name made lowercase.
    boys_kachi = models.FloatField(db_column='Boys_Kachi', blank=True, null=True)  # Field name made lowercase.
    boys_one = models.FloatField(db_column='Boys_One', blank=True, null=True)  # Field name made lowercase.
    boys_two = models.FloatField(db_column='Boys_Two', blank=True, null=True)  # Field name made lowercase.
    boys_three = models.FloatField(db_column='Boys_Three', blank=True, null=True)  # Field name made lowercase.
    boys_four = models.FloatField(db_column='Boys_Four', blank=True, null=True)  # Field name made lowercase.
    boys_five = models.FloatField(db_column='Boys_Five', blank=True, null=True)  # Field name made lowercase.
    fs_rs = models.CharField(db_column='FS/RS', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'cs_enrollment'

    def __str__(self):
        return f"{self.bemis_code}, {self.school_name}"

class CsTeacherKobo(models.Model):
    teacher_name = models.CharField(db_column='Teacher Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_present_at_the_time_visit = models.CharField(db_column='Teacher Present at the time visit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_attendance_age_last_month = models.CharField(db_column='Teacher Attendance %age last month', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_index = models.FloatField(db_column='_index', blank=True, null=True)  # Field renamed because it started with '_'.
    field_parent_table_name = models.CharField(db_column='_parent_table_name', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_parent_index = models.FloatField(db_column='_parent_index', blank=True, null=True)  # Field renamed because it started with '_'.
    field_submission_id = models.FloatField(db_column='_submission__id', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_uuid = models.CharField(db_column='_submission__uuid', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_submission_time = models.DateTimeField(db_column='_submission__submission_time', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_validation_status = models.CharField(db_column='_submission__validation_status', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_notes = models.CharField(db_column='_submission__notes', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_status = models.CharField(db_column='_submission__status', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_submitted_by = models.CharField(db_column='_submission__submitted_by', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.
    field_submission_version_field = models.CharField(db_column='_submission___version__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_submission_tags = models.CharField(db_column='_submission__tags', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'.

    class Meta:
        
        db_table = 'cs_teacher_kobo'


class DsWiseCsList(models.Model):
    scode = models.ForeignKey(CsInfo, on_delete=models.CASCADE, db_column='scode')
    # scode = models.CharField(db_column='sCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tehsil = models.CharField(db_column='Tehsil', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uc = models.CharField(db_column='UC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    school_name = models.CharField(db_column='School Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cat = models.CharField(db_column='Cat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(max_length=255, blank=True, null=True)
    ad = models.CharField(db_column='AD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ds = models.CharField(db_column='DS', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'ds_wise_cs_list'

    def __str__(self):
        return f"{self.scode}, {self.school_name}"


class Fieldstaffassignedcs(models.Model):
    staff_name = models.CharField(db_column='Staff_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=255, blank=True, null=True)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codes = models.CharField(db_column='Codes', max_length=255, blank=True, null=True)  # Field name made lowercase.
    assignedschools = models.IntegerField(db_column='AssignedSchools', blank=True, null=True)  # Field name made lowercase.

    class Meta:
       
        db_table = 'fieldstaffassignedcs'

    def __str__(self):
        return f"{self.staff_name}, {self.assignedschools}"

class MneChecklist(models.Model):
    start = models.DateTimeField(blank=True, null=True)
    end = models.DateTimeField(blank=True, null=True)
    today = models.DateTimeField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    date_of_visit = models.DateTimeField(db_column='Date of Visit', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    capture_gps_point = models.CharField(db_column='Capture GPS Point', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_capture_gps_point_latitude = models.FloatField(db_column='_Capture GPS Point_latitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_capture_gps_point_longitude = models.FloatField(db_column='_Capture GPS Point_longitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_capture_gps_point_altitude = models.FloatField(db_column='_Capture GPS Point_altitude', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    field_capture_gps_point_precision = models.FloatField(db_column='_Capture GPS Point_precision', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    bemis_code = models.ForeignKey(CsInfo, on_delete=models.CASCADE, db_column='scode')
    # bemis_code = models.CharField(db_column='BEMIS CODE', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    school_name = models.CharField(db_column='School Name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    district = models.CharField(db_column='District', max_length=255, blank=True, null=True)  # Field name made lowercase.
    contact_number_of_teacher = models.CharField(db_column='Contact number of teacher', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    select_found_open_at_the_time_of_visit = models.CharField(db_column='Select found open at the time of visit', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    select_one_if_school_is_closed = models.CharField(db_column='Select one if school is closed', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_teachers_appionted_in_the_school = models.FloatField(db_column='Number of Teachers appionted in the school', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    girls_enrollment_kachi_as_per_attendance_register_field = models.FloatField(db_column='Girls Enrollment Kachi (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_one_as_per_attendance_register_field = models.FloatField(db_column='Girls Enrollment One (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_two_as_per_attendance_register_field = models.FloatField(db_column='Girls Enrollment Two (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_three_as_per_attendance_register_field = models.FloatField(db_column='Girls Enrollment Three (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_four_as_per_attendance_register_field = models.FloatField(db_column='Girls Enrollment Four (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_five_as_per_attendance_register_field = models.FloatField(db_column='Girls Enrollment Five (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_kachi_as_per_attendance_register_field = models.FloatField(db_column='Boys Enrollment Kachi (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_one_as_per_attendance_register_field = models.FloatField(db_column='Boys Enrollment One (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_two_as_per_attendance_register_field = models.FloatField(db_column='Boys Enrollment Two (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_three_as_per_attendance_register_field = models.FloatField(db_column='Boys Enrollment Three (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_four_as_per_attendance_register_field = models.FloatField(db_column='Boys Enrollment Four (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_five_as_per_attendance_register_field = models.FloatField(db_column='Boys Enrollment Five (as per attendance register)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_kachi_present_at_the_time_of_visit_field = models.FloatField(db_column='Girls Enrollment Kachi (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_one_present_at_the_time_of_visit_field = models.FloatField(db_column='Girls Enrollment One (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_two_present_at_the_time_of_visit_field = models.FloatField(db_column='Girls Enrollment Two (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_three_present_at_the_time_of_visit_field = models.FloatField(db_column='Girls Enrollment Three (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_four_present_at_the_time_of_visit_field = models.FloatField(db_column='Girls Enrollment Four (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_enrollment_five_present_at_the_time_of_visit_field = models.FloatField(db_column='Girls Enrollment Five (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_kachi_present_at_the_time_of_visit_field = models.FloatField(db_column='Boys Enrollment Kachi (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_one_present_at_the_time_of_visit_field = models.FloatField(db_column='Boys Enrollment One (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_two_present_at_the_time_of_visit_field = models.FloatField(db_column='Boys Enrollment Two (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_three_present_at_the_time_of_visit_field = models.FloatField(db_column='Boys Enrollment Three (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_four_present_at_the_time_of_visit_field = models.FloatField(db_column='Boys Enrollment Four (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    boys_enrollment_five_present_at_the_time_of_visit_field = models.FloatField(db_column='Boys Enrollment Five (Present at the time of visit)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    girls_drop_out_last_month = models.FloatField(db_column='Girls drop out last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    boys_drop_out_last_month = models.FloatField(db_column='Boys drop out last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    girls_new_enrollment_last_month = models.FloatField(db_column='Girls New enrollment last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    boys_new_enrollment_last_month = models.FloatField(db_column='Boys New enrollment last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ptsmcoffie = models.CharField(db_column='PTSMCoffie', max_length=255, blank=True, null=True)  # Field name made lowercase.
    if_not_select_designation = models.CharField(db_column='if Not, Select designation', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    if_not_select_designation_president = models.FloatField(db_column='if Not, Select designation/President', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    if_not_select_designation_genereal_sect_field = models.FloatField(db_column='if Not, Select designation/Genereal Sect;', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    if_not_select_designation_vice_president = models.FloatField(db_column='if Not, Select designation/Vice president', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    if_not_select_designation_treasurer = models.FloatField(db_column='if Not, Select designation/Treasurer', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ptsmc_monthly_meeting_held_in_last_month = models.FloatField(db_column='PTSMC monthly meeting held in last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    amount_received_for_stationary = models.CharField(db_column='Amount received for Stationary', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stationary_amount = models.FloatField(db_column='Stationary Amount', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stationary_purchased_y_n = models.CharField(db_column='Stationary Purchased Y/N', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    purchase_date = models.DateTimeField(db_column='purchase Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stationary_available_with_students = models.CharField(db_column='Stationary Available with Students', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stationary_available_in_stock = models.CharField(db_column='Stationary Available in Stock', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stationary_receipt_available = models.CharField(db_column='Stationary Receipt Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_salary_amount_received_month_field = models.CharField(db_column='Teacher Salary Amount Received (Month)', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    note_book_provided_to_students_y_n = models.CharField(db_column='Note book provided to Students Y/N', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    note_book_checked_by_teacher_y_n = models.CharField(db_column='Note book checked by teacher Y/N', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    student_learning_performance = models.CharField(db_column='Student Learning performance', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    student_att_register_available = models.CharField(db_column='Student Att Register Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    student_att_register_updated = models.CharField(db_column='Student Att Register Updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_att_register_available = models.CharField(db_column='Teacher Att Register Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    teacher_att_register_updated = models.CharField(db_column='Teacher Att Register Updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    a_w_register_available = models.CharField(db_column='A&W Register Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    a_w_register_updated = models.CharField(db_column='A&W Register Updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cash_book_available = models.CharField(db_column='Cash book Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cash_book_updated = models.CharField(db_column='cash book Updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stock_register_available = models.CharField(db_column='Stock Register Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    stock_register_updated = models.CharField(db_column='Stock Register Updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logbook_available = models.CharField(db_column='Logbook Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    logbook_updated = models.CharField(db_column='Logbook Updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pec_monthly_meeting_register_available = models.CharField(db_column='PEC Monthly Meeting register Available', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pec_monthly_meeting_register_updated = models.CharField(db_column='PEC Monthly Meeting register updated', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    other_detail_information_if_any_field = models.TextField(db_column='Other Detail information (if any)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    select_visiting_staff_name = models.CharField(db_column='Select visiting staff name', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    select_region = models.CharField(db_column='Select Region', max_length=255, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    male_teacher_attendance_age_last_month = models.FloatField(db_column='Male teacher Attendance %age last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    female_teacher_attendance_age_last_month = models.FloatField(db_column='Female teacher Attendance %age last month', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_version_field = models.CharField(db_column='_version_', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_id = models.FloatField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_uuid = models.CharField(db_column='_uuid', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submission_time = models.DateTimeField(db_column='_submission_time', blank=True, null=True)  # Field renamed because it started with '_'.
    field_validation_status = models.CharField(db_column='_validation_status', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_notes = models.CharField(db_column='_notes', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_status = models.CharField(db_column='_status', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submitted_by = models.CharField(db_column='_submitted_by', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_version_field_0 = models.CharField(db_column='__version__', max_length=255, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row. Field renamed because it started with '_'. Field renamed because it ended with '_'. Field renamed because of name conflict.
    field_tags = models.CharField(db_column='_tags', max_length=255, blank=True, null=True)  # Field renamed because it started with '_'.
    field_index = models.FloatField(db_column='_index', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        
        db_table = 'mne_checklist'

    def __str__(self):
        return f"{self.bemis_code}, {self.school_name}, {self.date_of_visit}"

class Employee(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()  
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete = models.CASCADE )
   
    def __str__(self):  
        return f"{self.first_name}  -  {self.last_name}"  
    
    def get_absolute_url(self):
        return reverse('home')
    

