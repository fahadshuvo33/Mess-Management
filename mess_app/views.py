from django.shortcuts import render, redirect, reverse , get_object_or_404
from accounts.models import CustomUser, Mess
from mess_app.models import Bazar_List
from django.contrib.auth import get_user_model
from datetime import date



def members_info(request) :
    members = CustomUser.objects.filter(mess = request.user.mess)
    data = {
        'members' : members,
        }
    return render(request,'members_info.html' , data)



def meal_report(request) :
    return render(request, 'meal_report.html')



def summary(request) :
    return render(request, 'summary.html')



def add_bazar(request) :
    today_date = date.today().isoformat()
    users = CustomUser.objects.filter(mess = request.user.mess)
    data = {
        'today_date' : today_date,
        'users' : users
    }
    if request.method == 'POST' :
        dates = request.POST.get('date')
        user_id = request.POST.get('user')
        amount = request.POST.get('amount')
        note = request.POST.get('note')
        mess = request.user.mess

        bazar = Bazar_List(
            date = dates,
            user = get_object_or_404(CustomUser, id=user_id)
,
            amount = amount,
            note = note,
            mess = mess
        )
        bazar.save()
        return redirect('bazar_report')

    return render(request, 'add_bazar.html' , data)

def bazar_report(request) :
    bazars = Bazar_List.objects.filter(mess = request.user.mess)

    return render(request, 'bazar_report.html',{'bazars': bazars})