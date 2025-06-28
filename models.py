from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class StaffBase(AbstractUser):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    phone_number=models.CharField(max_length=15)



def __str__(self):
    return f"{self.first_name},{self.last_name},{self.date_of_birth},{self.phone_number}"    


class Manager (models.Model):
    user=models.ForeignKey(StaffBase, on_delete=models.CASCADE, related_name='manager')
    department = models.CharField(max_length=100)
    has_company_card=models.BooleanField(default='yes')

def get_role(self):
        return f"{self.deparment}"    


def __str__(self):
    return f"{self.department},{self.has_company_card}"


class Intern(models.Model):
    mentor=models.ForeignKey(Manager, on_delete=models.CASCADE)
    Internship_end=models.DateField(max_length=100)

    def get_role(self):
        return f"{self.internship_end}"

def __str__(self):
    return f"internship ends on{self.internship_end}"

# Create your models here.


#superuser login details
#name of user : oluwatimileyin
#password : 12345678iop