from django.forms import ModelForm
from .models import Employee
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        field='__all__'