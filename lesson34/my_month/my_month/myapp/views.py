from django.shortcuts import render
import calendar


def index(request):
    months = calendar.month_name
    return render(request, 'index.html', {'months': months, })