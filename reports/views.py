from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def return_civmto(request):
    #return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name':'Daniel Caparros'})
    #return render(request, 'templates/report_civmto.html', {'ReportName':'Access Track MTO'})
