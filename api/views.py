from django.shortcuts import render
from django.http import FileResponse
from django.http import JsonResponse
import json

def download_zip(response):

    zip = open(r'C:\Sandbox\dap\dap-backend\api\static\test.zip', 'rb')

    response = FileResponse(zip)

    return response


def turbine_list(request):
    """Return turbines."""
    json_data = open(r'C:\Sandbox\dap\dap-backend\dap_backend_api\static\turbines.json')
    data1 = json.load(json_data) # deserialises it   
    json_data.close()    
    return JsonResponse({"turbines":data1})


def report_list(request):
    """Return list of reports."""
    json_data = open(r'C:\Sandbox\dap\dap-backend\dap_backend_api\static\reports.json')
    data1 = json.load(json_data) # deserialises it   
    json_data.close()    
    return JsonResponse({"reports":data1})