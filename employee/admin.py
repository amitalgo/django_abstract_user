from django.contrib import admin
from .models import MyUser,UserBranch
from .forms import EmployeeChangeForm,EmployeeCreationForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserBranchInline(admin.StackedInline):
    model = UserBranch

class MyUserAdmin(BaseUserAdmin):
    form = EmployeeChangeForm
    add_form =EmployeeCreationForm

    inlines = [
        UserBranchInline
    ]
admin.site.register(MyUser,MyUserAdmin)