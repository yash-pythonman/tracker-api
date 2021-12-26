from django.contrib import admin
from organization.models import Employee, Organization, Department, Designation, OrganizationMember, \
    OrganizationAddress, EmployeeDepartment, EmployeeDesignation, UserAddress, Contact, ProfilePicture

admin.site.register(Organization)
admin.site.register(OrganizationMember)
admin.site.register(OrganizationAddress)
admin.site.register(Department)
admin.site.register(Designation)
admin.site.register(Employee)
admin.site.register(Contact)
admin.site.register(EmployeeDepartment)
admin.site.register(EmployeeDesignation)
admin.site.register(UserAddress)
admin.site.register(ProfilePicture)


