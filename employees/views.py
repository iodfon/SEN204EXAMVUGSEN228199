from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern

class StaffRolesView(APIView):
    def get(self, request):
        managers = Manager.objects.all()
        interns = Intern.objects.all()

        data = []
        for m in managers:
            data.append({'name': m.name, 'role': m.get_role()})
        for i in interns:
            data.append({'name': i.name, 'role': i.get_role(), 'mentor': i.mentor.name})

        return Response(data)
