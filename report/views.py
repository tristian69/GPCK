from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request,'report/report_list.html')

def report_create(request):

    return request

def report_read(request):
    return request



