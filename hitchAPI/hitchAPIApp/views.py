from django.shortcuts import render
from django.views import View
from django.http import JsonResponse

from .models import Company

class CompanyView(View):
    def get(self, request):
        clist = Company.objects.all()
        return JsonResponse(list(clist.values()), safe=False)

    def post(self, request):
        # post...
        return 0