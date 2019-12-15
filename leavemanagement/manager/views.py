from django.shortcuts import render, redirect


def ManagerHome(request):
    context={
        'title': "HomePage",
    }
    return render(request, 'manager/home.html', context=context)

def ManagerUser(request):
    context={
        'title': "LAMS",
    }
    return render(request, 'manager/user_select.html', context=context)