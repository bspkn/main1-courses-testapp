# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class CoursesDBManager(models.Manager):
	def validateAndCreate(self, data):
		newCourse = CoursesDB(course = data['name'], description = data['description'])
		newCourse.save()

class CoursesDB(models.Model):
	course = models.CharField(max_length = 64)
	description = models.CharField(max_length = 128)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = CoursesDBManager()
