from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Dataset
from . import serializers
from .pandasPractice import xlsxData

import json

class DatasetView(APIView):
    serializer_class = serializers.DatasetSerializer

    def get(self, request):
        print(request)
        dataset = Dataset.objects.all()
        return Response(list(dataset.values()))

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            nba = xlsxData() # Create the DataFrame object
            nba.readData(request.FILES['file']) # 0 Read nba.xlsx
            nba.data['Height'] = nba.data['Height'].dt.strftime('%Y-%m-%d')
            nba.printData()
            
            json_list = json.loads(json.dumps(list(nba.data.T.to_dict().values())))
            for dic in json_list:
                Dataset.objects.get_or_create(**dic)
            
            return Response("Succesfully uploaded")
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )