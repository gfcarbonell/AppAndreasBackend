# -*- encoding: utf-8 -*-
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ('user', 'rate', 'hour','active')
	search_fields  = ['user', 'rate']
	fieldsets = (
        ('Task Info', {'fields':('user', 'rate', 'hour','active')}),
    )

	class Meta:
		model = Task