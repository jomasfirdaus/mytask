from datetime import *
from django.shortcuts import render
from leave.models import RequestLeaveAprove
from travel.models import AproveTravelAutorization


#Your Code Here

def listamytask(request):
    context = {
        "pajina_mytask" : "active",
    }
    return render(request, 'mytask/mytask.html',context)


def leavestatus(request,status):
    status_request = None
    if status == 'Pending':
        status_request = "Review"
    elif status == 'Approved':
        status_request = "Acepted"
    elif status == "Rejected":
        status_request = "Rejected"

    dados = RequestLeaveAprove.objects.filter(contract=request.contract, status=status_request)

    context = {
        "pajina_mytask" : "active",
        "tab_leavestatus": "active",
        "tabstatus" : status,
        "dados": dados,
    }
    return render(request, 'mytask/mytask.html',context)


def travelstatus(request,status):
    status_request = None
    if status == 'Pending':
        status_request = "Review"
    elif status == 'Approved':
        status_request = "Acepted"
    elif status == "Rejected":
        status_request = "Rejected"

    dados = AproveTravelAutorization.objects.filter(contract=request.contract, status=status_request)

    context = {
        "pajina_mytask" : "active",
        "tab_travelstatus": "active",
        "tabstatus" : status,
        "dados": dados,
    }
    return render(request, 'mytask/mytask.html',context)