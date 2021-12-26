from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel, Address


class Organization(BaseModel):
    """
    Model created to store organization details
    """
    name = models.CharField(max_length=255)
    registration_no = models.CharField(max_length=255)
    pan_card = models.CharField(max_length=10)
    registration_date = models.DateField()
    logo = models.ImageField(upload_to="media", null=True, blank=True)

    class Meta:
        db_table = "organization"


class OrganizationMember(BaseModel):
    """
    Model created to store organization and member details.
    """
    member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="org_member")
    organization = models.ForeignKey(User, on_delete=models.CASCADE, related_name="member_org")

    class Meta:
        db_table = "organization_member"


class Department(BaseModel):
    """
    Model created to store department.
    """
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "department"


class Designation(BaseModel):
    """
    Model created to store designations.
    """
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "designation"


class Employee(BaseModel):
    """
    Model created to store the details of employee.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="base_user_for_user")
    emp_id = models.CharField(max_length=25)
    role = models.CharField(max_length=100)
    aadhar_number = models.CharField(max_length=12, null=True, blank=True)
    pan_card = models.CharField(max_length=10, null=True, blank=True)
    dl_number = models.CharField(max_length=100, null=True, blank=True)
    date_of_joining = models.DateField(null=True, blank=True)
    data_of_birth = models.DateField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="emp_org")

    class Meta:
        db_table = "employee"


class ProfilePicture(BaseModel):
    """
    Model created to store profile picture.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_image")
    image = models.ImageField(upload_to="media")
    is_current = models.BooleanField(default=True)

    class Meta:
        db_table = "profile_pic"


class EmployeeDepartment(BaseModel):
    """
    Model created to store employee and department details.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dep_emp")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="emp_dep")

    class Meta:
        db_table = "employee_department"


class EmployeeDesignation(BaseModel):
    """
    Model created to store employee and designation details.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="designation_emp")
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, related_name="emp_designation")

    class Meta:
        db_table = "employee_designation"


class Contact(BaseModel):
    """
    Model created to store details of organization's contact number.
    """
    base_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="number_of_user")
    number = models.CharField(max_length=13)
    is_primary = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=False)

    class Meta:
        db_table = "contact"


class UserAddress(Address):
    """
    Model created to store details of employee's address.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="address_of_user")

    class Meta:
        db_table = "user_address"


class OrganizationAddress(Address):
    """
    Model created to store details of organization's address.
    """
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="org_address")

    class Meta:
        db_table = "organization_address"
