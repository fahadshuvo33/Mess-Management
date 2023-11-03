from django.shortcuts import render, redirect, reverse , get_object_or_404
from accounts.models import CustomUser, Mess
from mess_app.models import Bazar_List, Meal
from django.contrib.auth import get_user_model
from datetime import date



def members_info(request) :
    members = CustomUser.objects.filter(mess = request.user.mess)
    data = {
        'members' : members,
        }
    return render(request,'members_info.html' , data)



def meal_sheet(request) :
    meals = Meal.objects.all()

    data = {
        'meals': meals,
    }
    return render(request, 'meal_sheet.html', data)



def dashboard(request) :
    return render(request, 'dashboard.html')



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

def all_bazar(request) :
    bazars = Bazar_List.objects.filter(mess = request.user.mess)

    return render(request, 'all_bazar.html',{'bazars': bazars})


def my_bazar(request) :
    bazars = Bazar_List.objects.filter(mess = request.user.mess, user = request.user)

    return render(request, 'all_bazar.html',{'bazars': bazars})


def utility(request) :
    return render(request, 'dashboard.html')