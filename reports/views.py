from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
def return_civmto(request):
    #return render(request, 'hello.html', {'name':'Daniel Caparros'})
    return render(request, 'report_civmto.html', {'ReportName':'Access Track MTO'})
