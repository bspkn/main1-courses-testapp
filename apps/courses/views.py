# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from models import CoursesDB

def index(request):
	allCourses = CoursesDB.objects.all()
	context = {
		'courses': allCourses,
	}
	return render(request, 'coursesApp/index.html', context)

def addCourse(request):
	if request.method == 'POST':
		CoursesDB.objects.validateAndCreate(request.POST)
	return redirect('/')

def checkDelete(request, id):
	context = {
		'courses': CoursesDB.objects.get(id = id),
	}
	return render(request, 'coursesApp/delete.html', context)

def delete(request, id):
	if request.method == 'POST':
		if request.POST['delete'] == 'yes':
			CoursesDB.objects.get(id = id).delete()
			return redirect('/')
		elif request.POST['delete'] == 'no':
			return redirect('/')
	
