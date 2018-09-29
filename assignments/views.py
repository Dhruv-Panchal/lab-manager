# -*- coding: utf-8 -*-

from . models import Assignments
from django.http import HttpResponse
from django.shortcuts import render

def assignment_list(request):
    assignments = Assignments.objects.all().order_by('date')
    return render(request,'assignments/assignment_list.html',{'assignments':assignments} )
# Create your views here.
def assignment_detail(request, slug):
    assignment = Assignments.objects.get(slug=slug)
    return render(request, 'assignments/assignment_detail.html',{'assignment':assignment})
