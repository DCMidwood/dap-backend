from django.shortcuts import render
from django.http import FileResponse

def download_zip(response):

    zip = open(r'C:\Sandbox\dap\dap-backend\api\static\test.zip', 'rb')

    response = FileResponse(zip)

    return response