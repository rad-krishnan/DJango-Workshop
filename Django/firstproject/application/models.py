from django.db import models

class Employee(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()

    def __str__(self):
        return self.empname

class Salary(models.Model):
    empno=models.ForeignKey(Employee,on_delete=models.CASCADE)
    salary=models.FloatField()
    month_year=models.CharField(max_length=20)

    
