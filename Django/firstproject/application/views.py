from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def addEmployee(request):
    forms=EmployeeForm()
    # if request.method=='POST':
    #     form=EmployeeForm(request.POST)
    return render(request,'addemp.html',
    {'forms':forms})