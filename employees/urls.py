from django.urls import path
from .views import StaffRolesView

urlpatterns = [
    path('roles/', StaffRolesView.as_view(), name='staff_roles'),
]
