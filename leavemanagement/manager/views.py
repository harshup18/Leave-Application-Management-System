from django.shortcuts import render, redirect


def ManagerHome(request):
    context={
        'title': "HomePage",
    }
    return render(request, 'manager/home.html', context=context)