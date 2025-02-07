# Generated by Django 5.0.7 on 2024-09-10 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employees", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empsalary",
            name="adhoc_allowance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="apfb",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="ara_2014",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="ara_2022",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="ara_2023",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="atp",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="basic_sal",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="convence_allowance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="cpfb",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="dra_2015",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="eobi_bef",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="eobi_emp",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="group_insurance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="house_rent",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="income_tax",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="med_allowance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="net_salary",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="pfcm",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="profit",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="provident_fund_balance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="provident_fund_bef",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="provident_fund_emp",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="special_allowance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="total_deduction",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="totall",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="utility_allowance",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="empsalary",
            name="wdpf",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
