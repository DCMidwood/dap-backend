from django.shortcuts import render

reports = [
    {'id': 1, 'report_name':'Total Gravel'},
    {'id': 2, 'report_name':'Total Lengths by Track Id'},
    {'id': 3, 'report_name':'example report' }
]



def home(request):
    context = {'reports': reports}
    return render(request, 'base/home.html', context)

def report(request,pk):
    report = None
    for i in reports:
        if i['id'] == int(pk):
            report = i
    context = {'report': report}

    return render(request, 'base/report.html', context)