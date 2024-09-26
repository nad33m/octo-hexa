# Generated by Django 5.0.7 on 2024-08-29 18:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CsInfo',
            fields=[
                ('scode', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('cat', models.CharField(blank=True, choices=[('Summer', 'Summer'), ('Winter', 'Winter')], db_column='Cat', max_length=255, null=True)),
                ('did', models.CharField(blank=True, db_column='DID', max_length=255, null=True)),
                ('tid', models.CharField(blank=True, db_column='TID', max_length=255, null=True)),
                ('ucid', models.CharField(blank=True, db_column='UCID', max_length=255, null=True)),
                ('vid', models.CharField(blank=True, db_column='VID', max_length=255, null=True)),
                ('phase', models.CharField(blank=True, db_column='Phase', max_length=255, null=True)),
                ('sname', models.CharField(blank=True, db_column='Sname', max_length=255, null=True)),
                ('region', models.CharField(blank=True, choices=[('Central-A', 'Central-A'), ('Central-B', 'Central-B'), ('South West-A', 'South West-A'), ('South West-B', 'South West-B'), ('South East-A', 'South East-A'), ('South East-B', 'South East-B'), ('North-A', 'North-A'), ('North-B', 'North-B')], max_length=255, null=True)),
                ('schoolstatus', models.CharField(blank=True, db_column='SchoolStatus', max_length=16, null=True)),
            ],
            options={
                'db_table': 'cs_info',
            },
        ),
        migrations.CreateModel(
            name='CsTeacherKobo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(blank=True, db_column='Teacher Name', max_length=255, null=True)),
                ('teacher_present_at_the_time_visit', models.CharField(blank=True, db_column='Teacher Present at the time visit', max_length=255, null=True)),
                ('teacher_attendance_age_last_month', models.CharField(blank=True, db_column='Teacher Attendance %age last month', max_length=255, null=True)),
                ('field_index', models.FloatField(blank=True, db_column='_index', null=True)),
                ('field_parent_table_name', models.CharField(blank=True, db_column='_parent_table_name', max_length=255, null=True)),
                ('field_parent_index', models.FloatField(blank=True, db_column='_parent_index', null=True)),
                ('field_submission_id', models.FloatField(blank=True, db_column='_submission__id', null=True)),
                ('field_submission_uuid', models.CharField(blank=True, db_column='_submission__uuid', max_length=255, null=True)),
                ('field_submission_submission_time', models.DateTimeField(blank=True, db_column='_submission__submission_time', null=True)),
                ('field_submission_validation_status', models.CharField(blank=True, db_column='_submission__validation_status', max_length=255, null=True)),
                ('field_submission_notes', models.CharField(blank=True, db_column='_submission__notes', max_length=255, null=True)),
                ('field_submission_status', models.CharField(blank=True, db_column='_submission__status', max_length=255, null=True)),
                ('field_submission_submitted_by', models.CharField(blank=True, db_column='_submission__submitted_by', max_length=255, null=True)),
                ('field_submission_version_field', models.CharField(blank=True, db_column='_submission___version__', max_length=255, null=True)),
                ('field_submission_tags', models.CharField(blank=True, db_column='_submission__tags', max_length=255, null=True)),
            ],
            options={
                'db_table': 'cs_teacher_kobo',
            },
        ),
        migrations.CreateModel(
            name='Fieldstaffassignedcs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_name', models.CharField(blank=True, db_column='Staff_Name', max_length=255, null=True)),
                ('designation', models.CharField(blank=True, db_column='Designation', max_length=255, null=True)),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('codes', models.CharField(blank=True, db_column='Codes', max_length=255, null=True)),
                ('assignedschools', models.IntegerField(blank=True, db_column='AssignedSchools', null=True)),
            ],
            options={
                'db_table': 'fieldstaffassignedcs',
            },
        ),
        migrations.CreateModel(
            name='CsEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('tehsil', models.CharField(blank=True, db_column='Tehsil', max_length=255, null=True)),
                ('uc', models.CharField(blank=True, db_column='UC', max_length=255, null=True)),
                ('school_name', models.CharField(blank=True, db_column='School_Name', max_length=255, null=True)),
                ('girls_kachi', models.FloatField(blank=True, db_column='Girls_Kachi', null=True)),
                ('girls_one', models.FloatField(blank=True, db_column='Girls_One', null=True)),
                ('girls_two', models.FloatField(blank=True, db_column='Girls_Two', null=True)),
                ('girls_three', models.FloatField(blank=True, db_column='Girls_Three', null=True)),
                ('girls_four', models.FloatField(blank=True, db_column='Girls_four', null=True)),
                ('girls_five', models.FloatField(blank=True, db_column='Girls_five', null=True)),
                ('boys_kachi', models.FloatField(blank=True, db_column='Boys_Kachi', null=True)),
                ('boys_one', models.FloatField(blank=True, db_column='Boys_One', null=True)),
                ('boys_two', models.FloatField(blank=True, db_column='Boys_Two', null=True)),
                ('boys_three', models.FloatField(blank=True, db_column='Boys_Three', null=True)),
                ('boys_four', models.FloatField(blank=True, db_column='Boys_Four', null=True)),
                ('boys_five', models.FloatField(blank=True, db_column='Boys_Five', null=True)),
                ('fs_rs', models.CharField(blank=True, db_column='FS/RS', max_length=255, null=True)),
                ('bemis_code', models.ForeignKey(db_column='scode', on_delete=django.db.models.deletion.CASCADE, to='app.csinfo')),
            ],
            options={
                'db_table': 'cs_enrollment',
            },
        ),
        migrations.CreateModel(
            name='Constructedschools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('cat', models.CharField(blank=True, db_column='Cat', max_length=255, null=True)),
                ('tehsil', models.CharField(blank=True, db_column='Tehsil', max_length=255, null=True)),
                ('uc', models.CharField(blank=True, db_column='UC', max_length=255, null=True)),
                ('village', models.CharField(blank=True, db_column='Village', max_length=255, null=True)),
                ('phase', models.CharField(blank=True, db_column='PHASE', max_length=255, null=True)),
                ('school_name', models.CharField(blank=True, db_column='School Name', max_length=255, null=True)),
                ('constructed', models.CharField(blank=True, db_column='Constructed', max_length=255, null=True)),
                ('coordinates_n', models.CharField(blank=True, db_column='Coordinates n', max_length=255, null=True)),
                ('coordinates_e', models.CharField(blank=True, db_column='Coordinates E', max_length=255, null=True)),
                ('bemis_code', models.ForeignKey(db_column='scode', on_delete=django.db.models.deletion.CASCADE, to='app.csinfo')),
            ],
            options={
                'db_table': 'constructedschools',
            },
        ),
        migrations.CreateModel(
            name='DsWiseCsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('tehsil', models.CharField(blank=True, db_column='Tehsil', max_length=255, null=True)),
                ('uc', models.CharField(blank=True, db_column='UC', max_length=255, null=True)),
                ('school_name', models.CharField(blank=True, db_column='School Name', max_length=255, null=True)),
                ('cat', models.CharField(blank=True, db_column='Cat', max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('ad', models.CharField(blank=True, db_column='AD', max_length=255, null=True)),
                ('ds', models.CharField(blank=True, db_column='DS', max_length=255, null=True)),
                ('scode', models.ForeignKey(db_column='scode', on_delete=django.db.models.deletion.CASCADE, to='app.csinfo')),
            ],
            options={
                'db_table': 'ds_wise_cs_list',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MneChecklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('today', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_visit', models.DateTimeField(blank=True, db_column='Date of Visit', null=True)),
                ('capture_gps_point', models.CharField(blank=True, db_column='Capture GPS Point', max_length=255, null=True)),
                ('field_capture_gps_point_latitude', models.FloatField(blank=True, db_column='_Capture GPS Point_latitude', null=True)),
                ('field_capture_gps_point_longitude', models.FloatField(blank=True, db_column='_Capture GPS Point_longitude', null=True)),
                ('field_capture_gps_point_altitude', models.FloatField(blank=True, db_column='_Capture GPS Point_altitude', null=True)),
                ('field_capture_gps_point_precision', models.FloatField(blank=True, db_column='_Capture GPS Point_precision', null=True)),
                ('school_name', models.CharField(blank=True, db_column='School Name', max_length=255, null=True)),
                ('district', models.CharField(blank=True, db_column='District', max_length=255, null=True)),
                ('contact_number_of_teacher', models.CharField(blank=True, db_column='Contact number of teacher', max_length=255, null=True)),
                ('select_found_open_at_the_time_of_visit', models.CharField(blank=True, db_column='Select found open at the time of visit', max_length=255, null=True)),
                ('select_one_if_school_is_closed', models.CharField(blank=True, db_column='Select one if school is closed', max_length=255, null=True)),
                ('number_of_teachers_appionted_in_the_school', models.FloatField(blank=True, db_column='Number of Teachers appionted in the school', null=True)),
                ('girls_enrollment_kachi_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Girls Enrollment Kachi (as per attendance register)', null=True)),
                ('girls_enrollment_one_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Girls Enrollment One (as per attendance register)', null=True)),
                ('girls_enrollment_two_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Girls Enrollment Two (as per attendance register)', null=True)),
                ('girls_enrollment_three_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Girls Enrollment Three (as per attendance register)', null=True)),
                ('girls_enrollment_four_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Girls Enrollment Four (as per attendance register)', null=True)),
                ('girls_enrollment_five_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Girls Enrollment Five (as per attendance register)', null=True)),
                ('boys_enrollment_kachi_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Boys Enrollment Kachi (as per attendance register)', null=True)),
                ('boys_enrollment_one_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Boys Enrollment One (as per attendance register)', null=True)),
                ('boys_enrollment_two_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Boys Enrollment Two (as per attendance register)', null=True)),
                ('boys_enrollment_three_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Boys Enrollment Three (as per attendance register)', null=True)),
                ('boys_enrollment_four_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Boys Enrollment Four (as per attendance register)', null=True)),
                ('boys_enrollment_five_as_per_attendance_register_field', models.FloatField(blank=True, db_column='Boys Enrollment Five (as per attendance register)', null=True)),
                ('girls_enrollment_kachi_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Girls Enrollment Kachi (Present at the time of visit)', null=True)),
                ('girls_enrollment_one_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Girls Enrollment One (Present at the time of visit)', null=True)),
                ('girls_enrollment_two_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Girls Enrollment Two (Present at the time of visit)', null=True)),
                ('girls_enrollment_three_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Girls Enrollment Three (Present at the time of visit)', null=True)),
                ('girls_enrollment_four_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Girls Enrollment Four (Present at the time of visit)', null=True)),
                ('girls_enrollment_five_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Girls Enrollment Five (Present at the time of visit)', null=True)),
                ('boys_enrollment_kachi_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Boys Enrollment Kachi (Present at the time of visit)', null=True)),
                ('boys_enrollment_one_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Boys Enrollment One (Present at the time of visit)', null=True)),
                ('boys_enrollment_two_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Boys Enrollment Two (Present at the time of visit)', null=True)),
                ('boys_enrollment_three_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Boys Enrollment Three (Present at the time of visit)', null=True)),
                ('boys_enrollment_four_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Boys Enrollment Four (Present at the time of visit)', null=True)),
                ('boys_enrollment_five_present_at_the_time_of_visit_field', models.FloatField(blank=True, db_column='Boys Enrollment Five (Present at the time of visit)', null=True)),
                ('girls_drop_out_last_month', models.FloatField(blank=True, db_column='Girls drop out last month', null=True)),
                ('boys_drop_out_last_month', models.FloatField(blank=True, db_column='Boys drop out last month', null=True)),
                ('girls_new_enrollment_last_month', models.FloatField(blank=True, db_column='Girls New enrollment last month', null=True)),
                ('boys_new_enrollment_last_month', models.FloatField(blank=True, db_column='Boys New enrollment last month', null=True)),
                ('ptsmcoffie', models.CharField(blank=True, db_column='PTSMCoffie', max_length=255, null=True)),
                ('if_not_select_designation', models.CharField(blank=True, db_column='if Not, Select designation', max_length=255, null=True)),
                ('if_not_select_designation_president', models.FloatField(blank=True, db_column='if Not, Select designation/President', null=True)),
                ('if_not_select_designation_genereal_sect_field', models.FloatField(blank=True, db_column='if Not, Select designation/Genereal Sect;', null=True)),
                ('if_not_select_designation_vice_president', models.FloatField(blank=True, db_column='if Not, Select designation/Vice president', null=True)),
                ('if_not_select_designation_treasurer', models.FloatField(blank=True, db_column='if Not, Select designation/Treasurer', null=True)),
                ('ptsmc_monthly_meeting_held_in_last_month', models.FloatField(blank=True, db_column='PTSMC monthly meeting held in last month', null=True)),
                ('amount_received_for_stationary', models.CharField(blank=True, db_column='Amount received for Stationary', max_length=255, null=True)),
                ('stationary_amount', models.FloatField(blank=True, db_column='Stationary Amount', null=True)),
                ('stationary_purchased_y_n', models.CharField(blank=True, db_column='Stationary Purchased Y/N', max_length=255, null=True)),
                ('purchase_date', models.DateTimeField(blank=True, db_column='purchase Date', null=True)),
                ('stationary_available_with_students', models.CharField(blank=True, db_column='Stationary Available with Students', max_length=255, null=True)),
                ('stationary_available_in_stock', models.CharField(blank=True, db_column='Stationary Available in Stock', max_length=255, null=True)),
                ('stationary_receipt_available', models.CharField(blank=True, db_column='Stationary Receipt Available', max_length=255, null=True)),
                ('teacher_salary_amount_received_month_field', models.CharField(blank=True, db_column='Teacher Salary Amount Received (Month)', max_length=255, null=True)),
                ('note_book_provided_to_students_y_n', models.CharField(blank=True, db_column='Note book provided to Students Y/N', max_length=255, null=True)),
                ('note_book_checked_by_teacher_y_n', models.CharField(blank=True, db_column='Note book checked by teacher Y/N', max_length=255, null=True)),
                ('student_learning_performance', models.CharField(blank=True, db_column='Student Learning performance', max_length=255, null=True)),
                ('student_att_register_available', models.CharField(blank=True, db_column='Student Att Register Available', max_length=255, null=True)),
                ('student_att_register_updated', models.CharField(blank=True, db_column='Student Att Register Updated', max_length=255, null=True)),
                ('teacher_att_register_available', models.CharField(blank=True, db_column='Teacher Att Register Available', max_length=255, null=True)),
                ('teacher_att_register_updated', models.CharField(blank=True, db_column='Teacher Att Register Updated', max_length=255, null=True)),
                ('a_w_register_available', models.CharField(blank=True, db_column='A&W Register Available', max_length=255, null=True)),
                ('a_w_register_updated', models.CharField(blank=True, db_column='A&W Register Updated', max_length=255, null=True)),
                ('cash_book_available', models.CharField(blank=True, db_column='Cash book Available', max_length=255, null=True)),
                ('cash_book_updated', models.CharField(blank=True, db_column='cash book Updated', max_length=255, null=True)),
                ('stock_register_available', models.CharField(blank=True, db_column='Stock Register Available', max_length=255, null=True)),
                ('stock_register_updated', models.CharField(blank=True, db_column='Stock Register Updated', max_length=255, null=True)),
                ('logbook_available', models.CharField(blank=True, db_column='Logbook Available', max_length=255, null=True)),
                ('logbook_updated', models.CharField(blank=True, db_column='Logbook Updated', max_length=255, null=True)),
                ('pec_monthly_meeting_register_available', models.CharField(blank=True, db_column='PEC Monthly Meeting register Available', max_length=255, null=True)),
                ('pec_monthly_meeting_register_updated', models.CharField(blank=True, db_column='PEC Monthly Meeting register updated', max_length=255, null=True)),
                ('other_detail_information_if_any_field', models.TextField(blank=True, db_column='Other Detail information (if any)', null=True)),
                ('select_visiting_staff_name', models.CharField(blank=True, db_column='Select visiting staff name', max_length=255, null=True)),
                ('select_region', models.CharField(blank=True, db_column='Select Region', max_length=255, null=True)),
                ('male_teacher_attendance_age_last_month', models.FloatField(blank=True, db_column='Male teacher Attendance %age last month', null=True)),
                ('female_teacher_attendance_age_last_month', models.FloatField(blank=True, db_column='Female teacher Attendance %age last month', null=True)),
                ('field_version_field', models.CharField(blank=True, db_column='_version_', max_length=255, null=True)),
                ('field_id', models.FloatField(blank=True, db_column='_id', null=True)),
                ('field_uuid', models.CharField(blank=True, db_column='_uuid', max_length=255, null=True)),
                ('field_submission_time', models.DateTimeField(blank=True, db_column='_submission_time', null=True)),
                ('field_validation_status', models.CharField(blank=True, db_column='_validation_status', max_length=255, null=True)),
                ('field_notes', models.CharField(blank=True, db_column='_notes', max_length=255, null=True)),
                ('field_status', models.CharField(blank=True, db_column='_status', max_length=255, null=True)),
                ('field_submitted_by', models.CharField(blank=True, db_column='_submitted_by', max_length=255, null=True)),
                ('field_version_field_0', models.CharField(blank=True, db_column='__version__', max_length=255, null=True)),
                ('field_tags', models.CharField(blank=True, db_column='_tags', max_length=255, null=True)),
                ('field_index', models.FloatField(blank=True, db_column='_index', null=True)),
                ('bemis_code', models.ForeignKey(db_column='scode', on_delete=django.db.models.deletion.CASCADE, to='app.csinfo')),
            ],
            options={
                'db_table': 'mne_checklist',
            },
        ),
        migrations.CreateModel(
            name='TeacherInfo',
            fields=[
                ('cnic', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('expiry_date', models.CharField(blank=True, max_length=255, null=True)),
                ('teacher_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, max_length=255, null=True)),
                ('account_no', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_code', models.FloatField(blank=True, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_code', models.CharField(blank=True, max_length=255, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_no', models.CharField(blank=True, max_length=255, null=True)),
                ('father_name', models.CharField(blank=True, max_length=255, null=True)),
                ('qualification', models.CharField(blank=True, choices=[('Matric', 'Matric'), ('Inter', 'Intermediate'), ('Graduate', 'Graduate'), ('Masters', 'Mssters')], max_length=255, null=True)),
                ('profq', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment_date', models.DateTimeField(blank=True, null=True)),
                ('birth_date', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('scode', models.ForeignKey(db_column='scode', on_delete=django.db.models.deletion.CASCADE, to='app.csinfo')),
            ],
            options={
                'db_table': 'teacher_info',
            },
        ),
    ]
