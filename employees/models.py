from django.db import models

# Create your models here.
from django.db import models

# Abstract Base Model
class StaffBase(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_joined = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

# Manager subclass
class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def get_role(self):
        return "Manager"

# Intern subclass
class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name="interns")
    internship_end = models.DateField()

    def get_role(self):
        return "Intern"
