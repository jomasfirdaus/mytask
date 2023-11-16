from datetime import *
from django.shortcuts import render
from leave.models import RequestLeaveAprove
from travel.models import AproveTravelAutorization


#Your Code Here

def listamytask(request):
    context = {
        "pajina_mytask" : "active",
        # "dadosta": dadosta,
    }
    return render(request, 'mytask/mytask.html',context)


def mytasktab(request,tab):
    context = {
        "pajina_mytask" : "active",
        "tab_"+str(tab): "active",
        "tab" : tab,
            }
    return render(request, 'mytask/mytask.html',context)


def mytaskpilltab(request,tab,status):
    dados = None
    
    if tab == 'leave':
        if status == 'pending':
            dados = RequestLeaveAprove.objects.filter(contract=request.contract, status='Review')
        elif status == 'aproved':
            dados = RequestLeaveAprove.objects.filter(contract=request.contract, status='Acepted')
        elif status == 'rejected':
            dados = RequestLeaveAprove.objects.filter(contract=request.contract, status='Rejected')
    
    elif tab == 'travel':
        if status == 'pending':
            dados = AproveTravelAutorization.objects.filter(contract=request.contract, status='Review')
        elif status == 'aproved':
            dados = AproveTravelAutorization.objects.filter(contract=request.contract, status='Acepted')
        elif status == 'rejected':
            dados = AproveTravelAutorization.objects.filter(contract=request.contract, status='Rejected')

    context = {
        "pajina_mytask" : "active",
        "tab_"+str(tab): "active",
        "tab" : tab,
        "pill_tab_"+str(status): "active",
        "pill_tab": status,
        "dados": dados,
            }
    return render(request, 'mytask/mytask.html',context)